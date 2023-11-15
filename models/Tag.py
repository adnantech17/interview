
class Tag:
    def __init__(self, id, publisher_id, tag):
        self.id = id
        self.publisher_id = publisher_id
        self.tag = tag

    def __str__(self):
        return f"Tag(id={self.id}, publisher_id={self.publisher_id}, tag='{self.tag}')"
