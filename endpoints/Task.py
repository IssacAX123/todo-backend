import yaml
from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_mysqldb import MySQL
import bcrypt


class Task(Resource):
    def __init__(self, **kwargs):
        self.mysql = kwargs["mysql"]
        self.cursor = self.mysql.connection.cursor()

    def get(self, user_id, task_id):
        self.cursor.execute(f"SELECT id, `name`, due_date FROM task WHERE id={task_id};")
        details = self.cursor.fetchone()
        self.cursor.close()
        return make_response(jsonify({"response": "success", "task": details}), 200)

    def post(self):
        user_id = request.form["user_id"]
        name = request.form["name"]
        due_date = request.form["due_date"]
        self.cursor.execute(f"INSERT INTO task(`name`, user_id, due_date) VALUES ('{name}', {user_id}, '{due_date}');")
        self.mysql.connection.commit()
        return make_response(jsonify({"response": "success"}), 200)

    def patch(self, user_id, task_id):
        for key in request.form:
            value = request.form[key]
            self.cursor.execute(f"UPDATE task SET {key}='{value}' WHERE id={task_id};")
            self.mysql.connection.commit()
            return make_response(jsonify({"response": "success"}), 200)

    def delete(self, user_id, task_id):
        self.cursor.execute(f"DELETE FROM task WHERE id={task_id};")
        self.mysql.connection.commit()
        return make_response(jsonify({"response": "success"}), 200)

