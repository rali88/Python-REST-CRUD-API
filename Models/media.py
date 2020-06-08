from db import db
class MediaModel(db.Model):
    
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    rank = db.Column(db.Float())
    genre = db.Column(db.String())
    store_id = db.Column(db.Integer(), db.ForeignKey('mediastore.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, rank, genre, store_id):
        self.name = name
        self.rank = rank
        self.type = genre
        self.store_id = store_id
    
    def jsonify(self):
        return {'name': self.name, 'rank': self.rank, 'genre': self.genre, 'store_id': self.store_id}

    @classmethod
    def get_one(cls, name):
        media = cls.query.filter_by(name=name).first()
        if media:
            return media

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
