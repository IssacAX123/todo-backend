import yaml
from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_mysqldb import MySQL
import bcrypt


class User(Resource):
    def __init__(self, **kwargs):
        self.mysql = kwargs["mysql"]
        self.cursor = self.mysql.connection.cursor()

    def get(self, email):
        password = request.form["password"]
        self.cursor.execute(f"SELECT password FROM user WHERE email='{email}'")
        hashed_password = self.cursor.fetchone()["password"]
        first_name = ""
        last_name = ""
        id = -1
        if bcrypt.checkpw(password.encode("utf-8"),hashed_password.encode("utf-8")):
            self.cursor.execute(f"SELECT id, first_name, last_name FROM user WHERE email='{email}'")
            details = self.cursor.fetchone()
            first_name = details["first_name"]
            last_name = details["last_name"]
            id = details["id"]
        self.cursor.close()
        return make_response(jsonify({"response": "success", "match": bcrypt.checkpw(password.encode("utf-8"),
                                                                                    hashed_password.encode(
                                                                                        "utf-8")), "first_name": first_name, "last_name": last_name, "email": email, "id": id}), 200)

    def post(self):
        for field in ['first_name', 'last_name', 'email', 'password']:
            if field not in request.form:
                return make_response(jsonify({"response": f"missing {field}"}), 200)
        r_firstname = request.form["first_name"]
        r_lastname = request.form["last_name"]
        r_email = request.form["email"]
        r_password = request.form["password"]
        r_password_hashed = bcrypt.hashpw(r_password.encode('utf-8'), bcrypt.gensalt()).decode("utf-8")
        self.cursor.execute(
            f"INSERT INTO user(first_name, last_name, email, password) VALUES ('{r_firstname}', '{r_lastname}','{r_email}', '{r_password_hashed}');")
        self.mysql.connection.commit()
        self.cursor.close()
        return make_response(jsonify({"response": "success"}), 200)
