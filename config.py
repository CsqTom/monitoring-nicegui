from typing import List, Tuple


class Config:
    # 后端地址
    API_BASE = "http://localhost:12309"

    # 系统配置
    APP_NAME = "监控管理系统"
    LOGO = "assets/logo.png"
    PORT = 5000

    # 路由配置 (路由名称, 显示名称, 组件路径)
    ROUTES: List[Tuple[str, str, str]] = [
        ("dashboard", "仪表盘",),
        ("users", "用户管理",),
        ("settings", "系统设置",)
    ]

    # 主题配置
    THEMES = {
        "default": {
            "primary": "#4CAF50",
            "secondary": "#8BC34A",
            "accent": "#CDDC39"
        },
        "dark": {
            "primary": "#424242",
            "secondary": "#212121",
            "accent": "#616161"
        },
        "blue": {
            "primary": "#2196F3",
            "secondary": "#64B5F6",
            "accent": "#90CAF9"
        },
    }

    # 登录配置
    LOGIN_ICON = "assets/login.svg"
    USER_MENU_ITEMS = [
        {"name": "个人中心", "icon": "account_circle"},
        {"name": "退出登录", "icon": "logout"}
    ]

    # 主题持久化配置
    @property
    def current_theme(self):
        return ui.run_javascript('localStorage.getItem("current_theme")') or 'default'


config = Config()
