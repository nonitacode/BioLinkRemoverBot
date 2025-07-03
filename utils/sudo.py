from config import OWNER_ID

def is_sudo(user_id: int) -> bool:
    return user_id == OWNER_ID
