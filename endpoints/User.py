from flask_restful import Resource
from flask import jsonify, make_response, request


class User(Resource):
    def get(self, username):
        return make_response(jsonify({"message": "hello"}), 200)

    def post(self):
        r_username = request.form["username"]
        return make_response(jsonify({"message": r_username}), 200)



