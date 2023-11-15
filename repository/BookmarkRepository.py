
from database import Database


class BookmarkRepository:
    def __init__(self):
        self.db = Database()

    def add_bookmark(self, bookmark):
        self.db.bookmarks.append(bookmark)

    def get_bookmarks_by_user_id(self, user_id):
        return [bookmark for bookmark in self.db.bookmarks if bookmark.user_id == user_id]
