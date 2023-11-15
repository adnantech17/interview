
class Bookmark:
    def __init__(self, id, user_id, publisher_id):
        self.id = id
        self.user_id = user_id
        self.publisher_id = publisher_id

    def __str__(self):
        return f"Bookmark(id={self.id}, user_id={self.user_id}, publisher_id={self.publisher_id})"
