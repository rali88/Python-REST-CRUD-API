from db import db
class StoreModel(db.Model):    
    
    __tablename__ = 'mediastore'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    items = db.relationship('MediaModel', lazy = 'dynamic')

    def __init__(self, name):
        self.name = name
    
    def jsonify(self):
        return {'store name': self.name, 'store items': list(map(lambda x: x.jsonify(),self.items.all())) }

    @classmethod
    def get_one(cls, name):
        store = cls.query.filter_by(name=name).first()
        if store:
            return store

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()