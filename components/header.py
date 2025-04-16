from nicegui import ui
from config import Config


class Header:
    def __init__(self):
        with ui.row().classes('w-full justify-between items-center transition-colors') as self.header:
            # 左侧LOGO和系统名称（固定宽度不扩展）
            with ui.row().classes('shrink-0 items-center gap-4'):
                ui.image(Config.LOGO).classes('w-10 h-10')
                ui.label(Config.APP_NAME).classes('text-xl font-bold')

            # 中间Tabs区域（占据剩余空间并居中）
            with ui.row().classes('flex-grow gap-4 text-lg font-medium'):
                self.current_route = 'dashboard'
                self.tabs = {}
                # 创建Tab项（增加间隔）
                with ui.tabs().classes('gap-4').bind_value(self, 'current_route').on_value_change(
                        lambda e: self.navigate(e.value)):
                    for route_name, display_name in Config.ROUTES:
                        tab = ui.tab(name=route_name, label=display_name)
                        self.tabs[route_name] = tab
                # 延迟加载初始化页面
                ui.timer(1.0, lambda: self.navigate(self.current_route), once=True)

            # 右侧功能区（固定宽度不扩展）
            with ui.row().classes('items-center gap-4'):
                # 用户登录状态
                with ui.button(icon='login'):
                    with ui.menu().classes('min-w-[100px]'):
                        with ui.menu_item().props('clickable'):
                            ui.icon('login').classes('mr-2')
                            ui.label('登录')
                            ui.menu_item().on('click', self.show_login)
                        ui.separator()
                        with ui.menu_item().props('clickable'):
                            ui.icon('logout').classes('mr-2')
                            ui.label('退出')
                            ui.menu_item().on('click', self.logout)

    def show_login(self):
        print('show login')
        pass

    def logout(self):
        print('logout')
        pass

    def navigate(self, route_name):
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
                from pages.settings_page.settings import Settings
                Settings()
