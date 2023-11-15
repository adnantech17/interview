
class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.users = []
            cls._instance.publishers = []
            cls._instance.tags = []
            cls._instance.bookmarks = []
        return cls._instance
