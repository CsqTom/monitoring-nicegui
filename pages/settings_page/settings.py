from nicegui import ui
from pages.settings_page.algorithm import AlgorithmConfig
from pages.settings_page.project import ProjectConfig
from pages.settings_page.device import DeviceConfig


class Settings:
    def __init__(self):
        self.selected_tab = 'algorithm'  # 添加状态变量

        with ui.row().classes("w-full h-[calc(100vh-4rem)]"):
            # 左侧导航 - 垂直Tab样式
            with ui.column().classes("w-64 bg-gray-100 h-full p-4"):
                ui.label("系统设置").classes("text-xl font-bold mb-2 text-gray-800")

                # 使用vertical tabs并绑定值
                with ui.tabs().props("vertical").bind_value(self, 'selected_tab').classes("w-full") as self.tabs:
                    ui.tab('algorithm', label="算法配置").classes("text-left justify-start tab-item")
                    ui.tab('project', label="项目配置").classes("text-left justify-start tab-item")
                    ui.tab('device', label="设备配置").classes("text-left justify-start tab-item")

            # 右侧内容区
            self.content = ui.column().classes("flex-1 p-6")

            # 绑定Tab切换事件
            self.tabs.on("update:model-value", lambda e: self.show_tab(e.args))
            self.show_tab(self.selected_tab)  # 使用状态变量初始化

    def show_tab(self, tab_name):
        self.selected_tab = tab_name  # 更新状态变量
        self.content.clear()
        with self.content:
            if tab_name == 'algorithm':
                AlgorithmConfig()
            elif tab_name == 'project':
                ProjectConfig()
            elif tab_name == 'device':
                DeviceConfig()

        # 添加自定义样式
        ui.add_head_html("""
        <style>
        /* 基础Tab样式 */
        .tab-item {
            padding: 12px 16px;
            margin-bottom: 4px;
            border-radius: 6px;
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            color: #4a5568;
        }

        /* 悬停状态 */
        .tab-item:hover {
            background-color: #edf2f7;
            color: #2d3748;
        }

        /* 选中状态 */
        .tab-item.q-tab--active {
            background-color: #4299e1 !important;
            color: white !important;
            font-weight: 500;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* 选中状态的左侧标记 
        .q-tab--active::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 4px;
            background-color: #1a365d;
            border-radius: 2px;
        }*/

        /* 移除默认的下划线 */
        .tab-item.q-tab__indicator {
            display: none !important;
        }
        </style>
        """)
