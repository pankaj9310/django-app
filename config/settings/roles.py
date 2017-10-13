from rolepermissions.roles import AbstractUserRole

class Manager(AbstractUserRole):
    available_permissions = {
        # 'create_contests': True,
        # 'create_problemsets': True,
        # 'edit_contests': True,
        # 'edit_problemsets': True,
        # 'delete_contests': True,
        # 'delete_problemsets': True,
        # 'update_contests': True,
        # 'update_problemsets': True,
    }
