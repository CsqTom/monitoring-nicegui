from nicegui import ui
import httpx
from config import Config


class AlgorithmConfig:
    def __init__(self):
        self.api_base = Config.API_BASE
        self.rows = []

        with ui.row().classes("w-full h-full gap-0"):
            # 左侧列表区域
            with ui.column().classes("w-64 bg-gray-100 p-2 h-full overflow-hidden"):
                with ui.card().classes("w-full h-full !rounded-none"):
                    with ui.row().classes("w-full justify-between items-center"):
                        ui.label("算法列表").classes("text-lg font-bold")
                        ui.button(icon="add", on_click=self.show_add_dialog).props("flat")

                    columns = [
                        {'name': 'id', 'label': 'ID', 'field': 'id'},
                        {'name': 'name', 'label': '名称', 'field': 'name'},
                    ]
                    self.table = ui.table(
                        columns=columns,
                        rows=self.rows,
                        row_key='id'
                    ).classes("w-full h-[calc(100%-80px)]")
                    self.table.on('rowClick', self.show_detail)

            # 右侧详情区域
            self.detail_column = ui.column().classes("flex-1 p-4 h-full overflow-auto")
            with self.detail_column:
                self.detail_card = ui.card().classes("w-full h-full")

            # 初始化加载数据
            ui.timer(0.1, self.load_data, once=True)

    async def load_data(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.api_base}/ai_list")
                if response.status_code == 200:
                    self.rows = response.json()["data"]
                    self.table.rows = self.rows
        except Exception as e:
            ui.notify(f"加载失败: {str(e)}", type="negative", position="top")

    async def show_detail(self, e):
        self.current_algorithm = e.args[1]
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.api_base}/ai_detail/{self.current_algorithm['id']}"
                )
                if response.status_code == 200:
                    detail = response.json()["data"]
                    self.detail_card.clear()
                    with self.detail_card:
                        ui.label("算法详情").classes("text-lg font-bold mb-4")
                        with ui.column().classes("w-full gap-4"):
                            self.name_input = ui.input(label="名称", value=detail['name'])
                            self.params_input = ui.number(label="参数", value=detail['params'])
                            with ui.row().classes("w-full justify-end gap-2"):
                                ui.button("删除", icon="delete",
                                          on_click=lambda: self.delete_algorithm(detail['id'])).props("outline")
                                ui.button("保存", icon="save", on_click=lambda: self.update_algorithm(detail['id']))
        except Exception as e:
            ui.notify(f"加载详情失败: {str(e)}", type="negative", position="top")

    async def show_add_dialog(self):
        with ui.dialog() as self.add_dialog, ui.card():
            with ui.column().classes("w-full gap-4"):
                ui.label("添加新算法").classes("text-lg font-bold")
                self.new_name = ui.input(label="名称")
                self.new_params = ui.number(label="参数")
                with ui.row().classes("w-full justify-end gap-2"):
                    ui.button("取消", on_click=self.add_dialog.close)
                    ui.button("确认", on_click=self.add_algorithm)
        self.add_dialog.open()

    async def add_algorithm(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_base}/ai_create",
                    json={"id": 0, "name": self.new_name.value, "params": self.new_params.value}
                )
                if response.status_code == 200:
                    self.add_dialog.close()
                    await self.load_data()
                    ui.notify("添加成功", type="positive", position="top")
                else:
                    raise Exception(response.json())
        except Exception as e:
            ui.notify(f"添加失败: {str(e)}", type="negative", position="top")

    async def update_algorithm(self, ai_id):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.put(
                    f"{self.api_base}/ai_upload/{ai_id}",
                    json={"id": ai_id, "name": self.name_input.value, "params": self.params_input.value}
                )
                if response.status_code == 200:
                    await self.load_data()
                    ui.notify("更新成功", type="positive", position="top")
        except Exception as e:
            ui.notify(f"更新失败: {str(e)}", type="negative", position="top")

    async def delete_algorithm(self, ai_id):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(f"{self.api_base}/ai_delete/{ai_id}")
                if response.status_code == 200:
                    await self.load_data()
                    self.detail_card.clear()
                    ui.notify("删除成功", type="positive", position="top")
        except Exception as e:
            ui.notify(f"删除失败: {str(e)}", type="negative", position="top")
