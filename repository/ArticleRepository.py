

from database import Database


class ArticleRepository:
    def __init__(self):
        self.db = Database()

    def add_article(self, article):
        self.db.articles.append(article)

    def get_articles_by_publisher_id(self, publisher_id):
        return [article for article in self.db.articles if article.publisher_id == publisher_id]
