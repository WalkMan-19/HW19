from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, rid: int):
        return self.dao.get_one(rid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        rid = data.get("id")
        director = self.dao.get_one(rid)

        director.name = data.get("name")

        self.dao.update(director)

    def update_partial(self, data):
        rid = data.get("id")
        director = self.dao.get_one(rid)

        if "name" in data:
            director.name = data.get("name")

        self.dao.update(director)

    def delete(self, rid):
        self.dao.delete(rid)
