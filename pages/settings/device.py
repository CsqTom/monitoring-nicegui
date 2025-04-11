from nicegui import ui

class DeviceConfig:
    def __init__(self):
        with ui.row().classes("w-full h-[calc(100vh-4rem)"):
            # 设备列表
            with ui.card().classes("w-full"):
                ui.label("设备列表").classes("text-lg font-bold")
                columns = [
                    {'name': 'sn', 'label': '序列号', 'field': 'sn'},
                    {'name': 'type', 'label': '设备类型', 'field': 'type'},
                ]
                rows = [
                    {'sn': 'CAM-001', 'type': '摄像头'},
                    {'sn': 'IPC-002', 'type': '智能相机'}
                ]
                self.table = ui.table(columns=columns, rows=rows, row_key='sn').classes("w-full")
                self.table.on('rowClick', self.show_detail)
            
            # 详情表单
            self.detail_card = ui.card().classes("w-full mt-4")
    
    def show_detail(self, e):
        with self.detail_card:
            ui.label("设备详情").classes("text-lg font-bold mb-4")
            ui.input(label="设备序列号", value=e.args[1]['sn'])
            ui.select(
                label="设备类型", 
                options=['摄像头', '智能相机', '传感器'],
                value=e.args[1]['type']
            )
            ui.number(label="采集频率(Hz)", value=30)
            ui.button("保存配置", icon="save")