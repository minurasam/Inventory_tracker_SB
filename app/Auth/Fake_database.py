# In a real app, this would connect to PostgreSQL, MySQL, etc.

fake_db = {}

def save_user(username: str, hashed_password: str):
    fake_db[username] = {"username": username, "password": hashed_password}

def get_user_by_username(username: str):
    return fake_db.get(username)
