
from database import Database


class BookmarkRepository:
    def __init__(self):
        self.db = Database()

    def addBookmark(self, bookmark):
        self.db.bookmarks.append(bookmark)

    def getBookmarksByUserId(self, user_id):
        return [bookmark for bookmark in self.db.bookmarks if bookmark.user_id == user_id]
