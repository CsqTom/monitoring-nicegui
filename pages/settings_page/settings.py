from nicegui import ui
from pages.settings_page.algorithm import AlgorithmConfig
from pages.settings_page.project import ProjectConfig
from pages.settings_page.device import DeviceConfig


class Settings:
    def __init__(self):
        self.selected_tab = 'algorithm'

        with ui.row().classes("w-full h-[calc(100vh-4rem)]"):
            # 左侧导航
            with ui.column().classes("w-64 bg-gray-100 h-full p-4"):
                ui.label("系统设置").classes("text-xl font-bold mb-2 text-gray-800")

                # 使用vertical tabs并绑定值
                # - vertical : 垂直排列选项卡 - active-color=primary : 激活状态使用主题主色 - text-color=grey-8 : 默认文字颜色为灰色
                # - active-bg-color=blue-100 : 激活项背景色为浅蓝色
                with ui.tabs().props(
                        "vertical active-color=primary text-color=grey-8 active-bg-color=blue-200"
                ).bind_value(self, 'selected_tab').classes("w-full") as self.tabs:
                    # - no-caps : 禁用自动大写转换 - dense : 紧凑模式，减少间距
                    ui.tab('algorithm', label="算法配置").props("no-caps dense").classes("text-left justify-start")
                    ui.tab('project', label="项目配置").props("no-caps dense").classes("text-left justify-start")
                    ui.tab('device', label="设备配置").props("no-caps dense").classes("text-left justify-start")

            # 右侧内容区
            self.content = ui.column().classes("flex-1 p-6")

            # 绑定Tab切换事件
            self.tabs.on("update:model-value", lambda e: self.show_tab(e.args))
            self.show_tab(self.selected_tab)

    def show_tab(self, tab_name):
        self.selected_tab = tab_name
        self.content.clear()
        with self.content:
            if tab_name == 'algorithm':
                AlgorithmConfig()
            elif tab_name == 'project':
                ProjectConfig()
            elif tab_name == 'device':
                DeviceConfig()
