
from database import Database


class PublisherRepository:
    def __init__(self):
        self.db = Database()

    def addPublisher(self, publisher):
        self.db.publishers.append(publisher)

    def getAllPublishers(self):
        return self.db.publishers

    def searchPublishersByName(self, name):
        return [publisher for publisher in self.db.publishers if name.lower() in publisher.name.lower()]

    def searchPublishersByTag(self, tag_name):
        return [publisher for publisher in self.db.publishers if any(tag.tag.lower() == tag_name.lower() for tag in self.db.tags)]

    def getPublisherById(self, publisherId):
        for publisher in self.db.publishers:
            if publisher.id == publisherId:
                return publisher
        return None

    def getPublisherByTag(self, tag_name):
        for publisher in self.db.publishers:
            for tag in publisher.tags:
                if tag.tag.lower() == tag_name.lower():
                    return publisher
        return None
