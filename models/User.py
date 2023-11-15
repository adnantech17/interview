class User:
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def __str__(self):
        return f"User(id={self.id}, email='{self.email}')"
