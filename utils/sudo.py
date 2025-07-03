from config import OWNER_ID

def is_sudo(user_id):
    return user_id == OWNER_ID
