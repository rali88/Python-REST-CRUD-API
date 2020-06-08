from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from Models.mediastore import StoreModel

class Store(Resource):

    @jwt_required()
    def get(self, name):
        try:
            store = StoreModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if store:
            return store.jsonify()
        return {'Message': 'Store not found'}, 404
    
    def post(self, name):
        try:
            store = StoreModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if store:
            return {'Message' : 'Store already exists, bad request'}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
            return {'Message': 'Successfull created'}, 201
        except:
            return {'Message':'Internal server error'}, 500

    def delete(self, name):
        try:
            store = StoreModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if store:
            try:
                store.delete_from_db()
                return {'Message' : 'Successfully deleted'}, 200
            except:
                return {'Message':'Internal server error'}, 500
        return {'Message' : 'Store not found'}, 404

class Storelist(Resource):
    def get(self):
        return {'media': list(map(lambda x: x.jsonify(), StoreModel.query.all()))}
