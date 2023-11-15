
from database import Database


class PublisherRepository:
    def __init__(self):
        self.db = Database()

    def add_publisher(self, publisher):
        self.db.publishers.append(publisher)

    def get_all_publishers(self):
        return self.db.publishers
