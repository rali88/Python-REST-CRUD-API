from db import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    password = db.Column(db.String())
    username = db.Column(db.String())
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        result = cls.query.filter_by(username=username).first()
        if result:
            user = result
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        result = cls.query.filter_by(id=_id).first()
        if result:
            user = result
        else:
            user = None
        return user
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()