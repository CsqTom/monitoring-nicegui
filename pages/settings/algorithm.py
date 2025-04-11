from nicegui import ui
import httpx


class AlgorithmConfig:
    def __init__(self):
        self.api_base = "http://localhost:12309"  # 后端API地址
        self.rows = []

        with ui.row().classes("w-full h-full gap-0"):
            # 左侧列表 (固定宽度)
            with ui.column().classes("w-64 bg-gray-100 p-2 h-full overflow-hidden"):
                with ui.card().classes("w-full h-full !rounded-none"):
                    ui.label("算法列表").classes("text-lg font-bold p-2")
                    columns = [
                        {'name': 'id', 'label': '算法id', 'field': 'id'},
                        {'name': 'name', 'label': '算法名称', 'field': 'name'},

                    ]
                    self.rows = [
                        {'id': ' ', 'name': ' '},
                    ]
                    self.table = ui.table(
                        columns=columns,
                        rows=self.rows,
                    ).classes("w-full h-[calc(100%-40px)]")
                    self.table.on('rowClick', self.show_detail)

            # 右侧详情 (弹性填充)
            self.detail_column = ui.column().classes("flex-1 p-4 h-full overflow-auto")
            with self.detail_column:
                self.detail_card = ui.card().classes("w-full h-full")

            # 初始化时加载数据
            ui.timer(0.1, self.load_data, once=True)

    async def load_data(self):
        try:
            async with httpx.AsyncClient() as client:
                # 获取算法列表
                response = await client.get(f"{self.api_base}/ai_list")
                if response.status_code == 200:
                    self.rows = response.json()["data"]
                    self.table.rows = self.rows
                    # if self.rows:
                    #     self.select_first_row()
        except Exception as e:
            ui.notify(f"加载数据失败: {str(e)}", type="negative")

    async def show_detail(self, e):
        self.current_algorithm = e.args[1]
        try:
            async with httpx.AsyncClient() as client:
                # 获取算法详情
                response = await client.get(
                    f"{self.api_base}/ai_detail/{self.current_algorithm['id']}"
                )
                if response.status_code == 200:
                    detail = response.json()["data"]
                    self.detail_card.clear()
                    with self.detail_card:
                        ui.label("算法详情").classes("text-lg font-bold mb-4")
                        with ui.column().classes("w-full gap-4"):
                            ui.input(label="算法名称", value=detail['name'])
                            ui.number(label="参数值", value=detail['params'])
                            with ui.row().classes("w-full justify-end"):
                                ui.button("保存配置", icon="save").props("unelevated")
        except Exception as e:
            ui.notify(f"加载详情失败: {str(e)}", type="negative")
