from database import Database


class UserRepository:
    def __init__(self):
        self.db = Database()

    def add_user(self, user):
        self.db.users.append(user)

    def get_all_users(self):
        return self.db.users
