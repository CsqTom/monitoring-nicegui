from nicegui import ui
from config import Config


class Header:
    def __init__(self):
        with ui.row().classes('w-full justify-between items-center px-4 h-16 shadow-sm bg-blue-500'):
            # 左侧LOGO和系统名称
            with ui.row().classes('items-center gap-4'):
                ui.image(Config.LOGO).classes('w-10 h-10')
                ui.label(Config.APP_NAME).classes('text-xl font-bold')

                self.current_route = 'dashboard'
                self.buttons = {}
                
                # Remove container classes here since they're now in main.py
                for route_name, display_name, _ in Config.ROUTES:
                    btn = ui.button(
                        display_name,
                        icon='home',
                        color='primary' if route_name == self.current_route else None,
                        on_click=lambda _, name=route_name: self.navigate(name)
                    ).props('flat full-width align=lefte')
                    self.buttons[route_name] = btn

                # 延迟1秒加载（解决初始化时布局未完成的问题）
                ui.timer(1.0, lambda: self.navigate(self.current_route), once=True)

            # 右侧功能区
            with ui.row().classes('items-center gap-4'):
                # 主题切换
                with ui.button(icon='color_lens').props('flat'):
                    with ui.menu().classes('min-w-[120px]'):
                        for theme_name in Config.THEMES:
                            with ui.menu_item().props('clickable').classes('min-w-full') as item:
                                ui.icon(theme_name.lower()).classes('mr-2')
                                ui.label(theme_name)
                                item.on('click', lambda _, name=theme_name: self.change_theme(name))

                # 用户登录状态
                with ui.button(icon='login').props('flat'):
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

    def change_theme(self, theme_name):
        print(f'change theme to {theme_name}')

        theme = Config.THEMES[theme_name]
        ui.colors(
            primary=theme["primary"],
            secondary=theme["secondary"],
            accent=theme["accent"]
        )
        ui.run_javascript(f"""
               document.documentElement.style.setProperty('--primary', '{theme["primary"]}');
               document.documentElement.style.setProperty('--secondary', '{theme["secondary"]}');
               document.documentElement.style.setProperty('--accent', '{theme["accent"]}');
           """)
        ui.update()

    def show_login(self):
        print('show login')
        pass

    def logout(self):
        print('logout')
        pass

    def navigate(self, route_name):
        # 更新按钮状态
        for name, btn in self.buttons.items():
            btn._props['color'] = 'primary' if name == route_name else None  
            # 更改背景色
            if name == route_name:
                btn.style('background-color: #f0f0f0;')  # 选中时的背景色
            else:
                btn.style('background-color: transparent;')  # 未选中时的背景色
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
                from pages.settings.settings import Settings
                Settings()