from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Api
import yaml
from endpoints.User import User
from endpoints.TaskList import TaskList
from endpoints.Task import Task
app = Flask(__name__)
api = Api(app)
db = yaml.load(open("endpoints/config.yaml"))
app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
api.add_resource(User, '/api/v1/user/<string:email>', endpoint='get-user', methods=['GET'], resource_class_kwargs={"mysql": mysql})
api.add_resource(User, '/api/v1/user/create', endpoint='create-user', methods=['POST'], resource_class_kwargs={"mysql": mysql})
api.add_resource(TaskList, '/api/v1/task/<string:user_id>/all', endpoint='get-tasklist', methods=['GET'], resource_class_kwargs={"mysql": mysql})
api.add_resource(Task, '/api/v1/task/<string:user_id>/<string:task_id>', endpoint='get-task', methods=['GET', 'DELETE'], resource_class_kwargs={"mysql": mysql})
api.add_resource(Task, '/api/v1/task/create', endpoint='create_task', methods=['POST'], resource_class_kwargs={"mysql": mysql})
api.add_resource(Task, '/api/v1/task/<string:user_id>/<string:task_id>', endpoint='update-task', methods=['PATCH'], resource_class_kwargs={"mysql": mysql})

if __name__ == '__main__':
    app.run(debug=True)
