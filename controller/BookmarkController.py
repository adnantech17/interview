# 3. controller/bookmark_controller.py
from repository import BookmarkRepository
from models import Bookmark


class BookmarkController:
    def __init__(self):
        self._bookmark_repository = BookmarkRepository()

    def addBookmark(self, user_id, publisher_id):
        id = len(self._bookmark_repository.getBookmarksByUserId(user_id)) + 1
        bookmark = Bookmark(id, user_id, publisher_id)
        self._bookmark_repository.addBookmark(bookmark)
        return {
            'data': bookmark,
            'message': 'Bookmark added successfully',
            'code': 200,
        }

    def getBookmarksByUserId(self, user_id):
        bookmarks = self._bookmark_repository.getBookmarksByUserId(user_id)
        return {
            'data': bookmarks,
            'message': 'Get Bookmarks Success',
            'code': 200,
        }
