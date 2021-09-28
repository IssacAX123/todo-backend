from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_mysqldb import MySQL




class Task(Resource):
    def __init__(self, **kwargs):
        self.mysql = MySQL(kwargs['app'])

    def get(self, id):
        return make_response(jsonify({"message": "hello"}), 200)

    def post(self):
        for field in ['first_name', 'last_name', 'email', 'password']:
            if field not in request.form:
                return make_response(jsonify({"response": f"missing {field}"}), 200)
        r_firstname = request.form["first_name"]
        r_lastname = request.form["last_name"]
        r_email = request.form["email"]
        r_password = request.form["password"]
        cursor = self.mysql.connection.cursor()
        cursor.execute(f"INSERT INTO user(first_name, last_name, email, password) VALUES ('{r_firstname}', '{r_lastname}', '{r_email}', '{r_password}');")
        self.mysql.connection.commit()
        cursor.close()
        return make_response(jsonify({"response": "success"}), 200)
