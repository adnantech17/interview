from database import Database


class UserRepository:
    def __init__(self):
        self.db = Database()

    def addUser(self, user):
        self.db.users.append(user)

    def getAllUsers(self):
        return self.db.users

    def getUserByEmail(self, email):
        for user in self.db.users:
            if user.email == email:
                return user
        return None
