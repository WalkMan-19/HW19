from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, rid: int):
        return self.session.query(Genre).get(rid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()

    def delete(self, rid):
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()
