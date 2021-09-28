import yaml
from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_mysqldb import MySQL
import bcrypt


class TaskList(Resource):
    def __init__(self, **kwargs):
        self.mysql = kwargs["mysql"]
        self.cursor = self.mysql.connection.cursor()

    def get(self, user_id):
        self.cursor.execute(f"SELECT id, `name`, due_date FROM task WHERE user_id='{user_id}'")
        details = self.cursor.fetchall()
        detail_list = list(details)
        self.cursor.close()
        return make_response(jsonify({"response": "success", "tasks": detail_list}), 200)

