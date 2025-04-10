from nicegui import ui
from config import Config


class Header:
    def __init__(self):
        with ui.row().classes('w-full justify-between items-center px-4 h-16 shadow-sm bg-white'):
            # 左侧LOGO和系统名称
            with ui.row().classes('items-center gap-4'):
                ui.image(Config.LOGO).classes('w-10 h-10')
                ui.label(Config.APP_NAME).classes('text-xl font-bold text-primary')

            # 右侧功能区
            with ui.row().classes('items-center gap-4'):
                # 主题切换
                with ui.button(icon='color_lens').props('flat'):
                    with ui.menu().classes('min-w-[120px]'):
                        for theme_name in Config.THEMES:
                            with ui.menu_item().props('clickable').classes('min-w-full'):
                                ui.icon(theme_name.lower()).classes('mr-2')  # 假设图标的名称是小写的主题名称
                                ui.label(theme_name)
                                ui.menu_item().on('click', lambda _, name=theme_name: self.change_theme(name))

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
        theme = Config.THEMES[theme_name]
        ui.colors(
            primary=theme["primary"],
            secondary=theme["secondary"],
            accent=theme["accent"]
        )
        # 强制更新页面样式
        ui.run_javascript('''
            document.documentElement.style.setProperty('--q-primary', arguments[0]);
            document.documentElement.style.setProperty('--q-secondary', arguments[1]);
            document.documentElement.style.setProperty('--q-accent', arguments[2]);
        ''', theme["primary"], theme["secondary"], theme["accent"])

    def show_login(self):
        print('show login')
        pass

    def logout(self):
        print('logout')
        pass
