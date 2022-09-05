from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, rid: int):
        return self.dao.get_one(rid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        rid = data.get("id")
        genre = self.dao.get_one(rid)

        genre.name = data.get("name")

        self.dao.update(genre)

    def update_partial(self, data):
        rid = data.get("id")
        genre = self.dao.get_one(rid)

        if "name" in data:
            genre.name = data.get("name")

        self.dao.update(genre)

    def delete(self, rid):
        self.dao.delete(rid)
