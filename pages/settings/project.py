from nicegui import ui

class ProjectConfig:
    def __init__(self):
        with ui.column().classes("w-full"):
            # 项目列表
            with ui.card().classes("w-full"):
                ui.label("项目列表").classes("text-lg font-bold")
                columns = [
                    {'name': 'id', 'label': 'ID', 'field': 'id'},
                    {'name': 'name', 'label': '项目名称', 'field': 'name'},
                ]
                rows = [
                    {'id': 1, 'name': '智慧园区'},
                    {'id': 2, 'name': '工业质检'}
                ]
                self.table = ui.table(columns=columns, rows=rows, row_key='id').classes("w-full")
                self.table.on('rowClick', self.show_detail)
            
            # 详情表单
            self.detail_card = ui.card().classes("w-full mt-4")
    
    def show_detail(self, e):
        with self.detail_card:
            ui.label("项目详情").classes("text-lg font-bold mb-4")
            ui.input(label="项目名称", value=e.args[1]['name'])
            # ui.date(label="开始时间").classes("w-full")
            ui.textarea(label="项目描述")
            ui.button("保存配置", icon="save")