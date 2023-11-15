class Publisher:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Publisher(id={self.id}, name='{self.name}', tags={self.tags})"
