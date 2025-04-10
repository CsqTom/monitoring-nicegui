from nicegui import ui

class Users:
    def __init__(self):
        ui.label('用户管理').classes('text-2xl font-bold')
        with ui.table(columns=[
            {'name': 'id', 'label': 'ID', 'field': 'id'},
            {'name': 'name', 'label': '姓名', 'field': 'name'},
            {'name': 'role', 'label': '角色', 'field': 'role'}
        ], rows=[
            {'id': 1, 'name': '张三', 'role': '管理员'},
            {'id': 2, 'name': '李四', 'role': '用户'}
        ]).classes('w-full'):
            pass