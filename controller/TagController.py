# 3. controller/tag_controller.py
from repository import TagRepository
from models import Tag


class TagController:
    def __init__(self):
        self._tagRepository = TagRepository()

    def addTag(self, publisherId, tagName):
        id = len(self._tagRepository.getAllTags()) + 1
        tag = Tag(id, publisherId, tagName)
        self._tagRepository.addTag(tag)
        return {
            'data': tag,
            'message': f'Tag added to Publisher {publisherId} successfully',
            'code': 200,
        }
