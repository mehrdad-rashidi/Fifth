from flask_restful import Resource, reqparse
import sqlite3

items = []


class ItemList(Resource):
    def get(self):
        return {'items': items}
