from nicegui import ui
from components.sidebar import Sidebar
from components.header import Header
from config import config

# ui.add_head_html('<link rel="stylesheet" href="/assets/styles.css">')

# 添加固定布局容器
with ui.row().classes('w-full h-screen'):
    # 修正布局结构
    with ui.column().classes('w-full h-full'):
        Header()  # 顶部导航栏
        
        with ui.row().classes('w-full h-[calc(100vh-4rem)]'):
            # 侧边栏容器
            with ui.column().classes('flex-none w-64 h-full bg-gray-100'):
                sidebar = Sidebar()
            
            # 内容区容器
            with ui.column().classes('flex-1 p-4'):
                ui.context.client.content = ui.column().classes('w-full h-full')

ui.run(port=config.PORT)
