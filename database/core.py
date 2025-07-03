whitelist = set()
violations = {}

def add_to_whitelist(user_id):
    whitelist.add(user_id)

def remove_from_whitelist(user_id):
    whitelist.discard(user_id)

def is_whitelisted(user_id):
    return user_id in whitelist

def increment_violations(user_id):
    violations[user_id] = violations.get(user_id, 0) + 1
    return violations[user_id]

def get_all_whitelist():
    return list(whitelist)
