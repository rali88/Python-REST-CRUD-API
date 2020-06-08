from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from Models.media import MediaModel

class Media(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('rank', type=float)
    parser.add_argument('genre')
    parser.add_argument('store_id', type=int)

    @jwt_required()
    def get(self, name):
        try:
            media = MediaModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if media:
            return media.jsonify()
        return {'Message': 'Media not found'}, 404
    
    def post(self, name):
        try:
            media = MediaModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if media:
            return {'Message' : 'Media already exists, bad request'}, 400
        data = Media.parser.parse_args()
        media = MediaModel(name, **data)
        try:
            media.save_to_db()
            return {'Message': 'Successfull created'}, 201
        except:
            return {'Message':'Internal server error'}, 500

    def delete(self, name):
        try:
            media = MediaModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if media:
            try:
                media.delete_from_db()
                return {'Message' : 'Successfully deleted'}, 200
            except:
                return {'Message':'Internal server error'}, 500
        return {'Message' : 'Media not found'}, 404
    
    def put(self, name):
        data = Media.parser.parse_args()
        try:
            media = MediaModel.get_one(name)
        except:
            return {'Message':'Internal server error'}, 500
        if media:
            updated = True
            media.rank = data['rank']
            media.genre = data['genre'] 
        else:
            updated = False
            media = MediaModel(name, **data)
        media.save_to_db()
        if updated:
            return {'Message': 'Successfully updated'}, 200
        return {'Message': 'Successfull created'}, 201

class Medialist(Resource):
    def get(self):
        return {'media': list(map(lambda x: x.jsonify(), MediaModel.query.all()))}
