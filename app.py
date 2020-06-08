from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity 
from Resources.user import UserRegister
from Resources.media import Media, Medialist
from Resources.mediastore import Store, Storelist
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rehan'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Media, '/media/<string:name>')
api.add_resource(Medialist, '/medialist')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Storelist, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)