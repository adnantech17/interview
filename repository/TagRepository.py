
from database import Database


class TagRepository:
    def __init__(self):
        self.db = Database()

    def addTag(self, tag):
        self.db.tags.append(tag)

    def getAllTags(self):
        return self.db.tags
