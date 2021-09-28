from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Api
import yaml
from endpoints.User import User
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

if __name__ == '__main__':
    app.run(debug=True)
