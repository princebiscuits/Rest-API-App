from flask_restful import Resource, reqparse
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Store not found'}, 404
        
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name {} already exists.".format(name)}, 400
        # data = Store.parser.parse_args()
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred inserting the store.'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}