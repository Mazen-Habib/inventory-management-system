
class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def check_password(self, password):
        return self.password == password
users = [
    User("admin", "adminpass", is_admin=True),
    User("user1", "userpass", is_admin=False)
]

def authenticate(username, password):
    for user in users:
        if user.username == username and user.check_password(password):
            return user
    return None
