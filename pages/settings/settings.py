from nicegui import ui
from .algorithm import AlgorithmConfig
from .project import ProjectConfig
from .device import DeviceConfig

class Settings:
    def __init__(self):
        with ui.row().classes("w-full h-[calc(100vh-4rem)]"):
            # 左侧导航
            with ui.column().classes("w-64 bg-gray-100 p-4"):
                ui.label("系统设置").classes("text-xl font-bold mb-4")
                ui.button("算法配置", on_click=lambda: self.show_tab('algorithm'))
                ui.button("项目配置", on_click=lambda: self.show_tab('project'))
                ui.button("设备配置", on_click=lambda: self.show_tab('device'))
            
            # 右侧内容区
            self.content = ui.column().classes("flex-1 p-4")
            self.show_tab('algorithm')  # 默认显示算法配置
    
    def show_tab(self, tab_name):
        self.content.clear()
        with self.content:
            if tab_name == 'algorithm':
                AlgorithmConfig()
            elif tab_name == 'project':
                ProjectConfig()
            elif tab_name == 'device':
                DeviceConfig()