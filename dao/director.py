from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, rid: int):
        return self.session.query(Director).get(rid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()
