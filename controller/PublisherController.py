# 3. controller/publisher_controller.py
from repository import PublisherRepository
from repository import TagRepository
from models import Publisher, Tag


class PublisherController:
    def __init__(self):
        self._publisherRepository = PublisherRepository()

    def register(self, name):
        id = len(self._publisherRepository.getAllPublishers()) + 1
        publisher = Publisher(id, name)
        self._publisherRepository.addPublisher(publisher)
        return {
            'data': publisher,
            'message': 'Publisher Register Success',
            'code': 201,
        }

    def searchPublisherByName(self, name):
        publishers = self._publisherRepository.searchPublishersByName(name)
        return {
            'data': publishers,
            'message': 'Search Success',
            'code': 200,
        }

    def searchPublisherByTag(self, tagName):
        publishers = self._publisherRepository.searchPublishersByTag(
            tagName)
        return {
            'data': publishers,
            'message': 'Search Success',
            'code': 200,
        }
