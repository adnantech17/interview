
from database import Database


class TagRepository:
    def __init__(self):
        self.db = Database()

    def add_tag(self, tag):
        self.db.tags.append(tag)

    def get_all_tags(self):
        return self.db.tags
