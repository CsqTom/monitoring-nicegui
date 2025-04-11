from nicegui import ui, app
from nicegui_toolkit.layout_tool import inject_layout_tool

inject_layout_tool()

with ui.card(), ui.row():
    ui.avatar("home")
    with ui.row():
        ui.label("数据大宇宙")
        ui.icon("mail")
        ui.label("发消息")
        
    with ui.row():
        ui.button("充电")
        ui.button("+关注67g")

ui.run()
