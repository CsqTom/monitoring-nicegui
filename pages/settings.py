from nicegui import ui

class Settings:
    def __init__(self):
        ui.label('系统设置').classes('text-2xl font-bold')
        with ui.card().classes('w-full'):
            ui.toggle(['启用通知', '禁用通知'])
            ui.toggle(['暗黑模式', '明亮模式'])
            ui.button('保存设置').classes('mt-4')