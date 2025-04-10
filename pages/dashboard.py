from nicegui import ui

class Dashboard:
    def __init__(self):
        ui.label('仪表盘').classes('text-2xl font-bold')
        with ui.row().classes('w-full'):
            ui.card().classes('w-1/3 h-32').style('background-color: #4CAF50')
            ui.card().classes('w-1/3 h-32').style('background-color: #8BC34A')
            ui.card().classes('w-1/3 h-32').style('background-color: #CDDC39')