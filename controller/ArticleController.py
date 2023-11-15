# 3. controller/article_controller.py
from repository import ArticleRepository
from models import Article


class ArticleController:
    def __init__(self):
        self._articleRepository = ArticleRepository()

    def addArticle(self, publisherId, title, description, publishDate):
        id = len(self._articleRepository.getArticle()) + 1
        article = Article(id, publisherId, title, description, publishDate)
        self._articleRepository.addArticle(article)
        return {
            'data': article,
            'message': 'Article added successfully',
            'code': 200,
        }

    def getArticlesByPublisherId(self, publisherId):
        articles = self._articleRepository.getArticleByPublisherId(
            publisherId)
        return {
            'data': articles,
            'message': 'Get Articles Success',
            'code': 200,
        }
