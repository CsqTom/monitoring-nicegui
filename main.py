from nicegui import ui
from components.sidebar import Sidebar
from components.header import Header
from config import config

# Create main layout
with ui.header().classes('justify-between items-center'):
    from components.header import Header

    Header()

# 添加固定布局容器
with ui.row().classes('w-full h-[calc(100vh-4rem)] flex-nowrap'):
    # 侧边栏容器 (固定宽度)
    with ui.column().classes('h-full bg-gray-100 w-64 flex-none'):
        sidebar = Sidebar()

    # 内容区容器 (弹性填充)
    with ui.column().classes('flex-1 h-full p-4 overflow-auto'):
        ui.context.client.content = ui.column().classes('w-full h-full')

ui.run(port=config.PORT)
