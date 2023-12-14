import sqlite3

from flask_restful import Resource, reqparse


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")

    def post(self):
        connection = sqlite3.connect('identifier.sqlite')
        cursor = connection.cursor()

        data = UserRegister.parser.parse_args()
        query = "INSERT INTO user VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()

        return {"massage": "User created successfully"}, 201
