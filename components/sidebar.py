from nicegui import ui
from config import Config

class Sidebar:
    def __init__(self):
        self.current_route = 'dashboard'
        self.buttons = {}
        
        # Remove container classes here since they're now in main.py
        for route_name, display_name, _ in Config.ROUTES:
            btn = ui.button(
                display_name,
                icon='home',
                color='primary' if route_name == self.current_route else None,
                on_click=lambda _, name=route_name: self.navigate(name)
            ).props('flat full-width align=left')
            self.buttons[route_name] = btn

    def navigate(self, route_name):
        # 更新按钮状态
        for name, btn in self.buttons.items():
            btn._props['color'] = 'primary' if name == route_name else None
            btn.update()
        
        # 更新内容区
        content = ui.context.client.content
        content.clear()
        with content:
            if route_name == 'dashboard':
                from pages.dashboard import Dashboard
                Dashboard()
            elif route_name == 'users':
                from pages.users import Users
                Users()
            elif route_name == 'settings':
                from pages.settings import Settings
                Settings()