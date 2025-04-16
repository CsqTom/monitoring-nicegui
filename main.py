from nicegui import ui
# from nicegui_toolkit.layout_tool import inject_layout_tool

# inject_layout_tool()


from config import config

# Create main layout
with ui.header().classes('justify-between items-center'):
    from components.header import Header

    Header()

# 添加固定布局容器
with ui.row().classes('w-full h-[calc(100vh-7rem)] flex-nowrap'):
    # 内容区容器 (弹性填充)
    with ui.column().classes('flex-1 h-full overflow-auto'):
        ui.context.client.content = ui.column().classes('w-full h-full')

ui.run(port=config.PORT)
