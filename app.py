from flask import Flask
from flask_restful import Api
from endpoints.User import User
import yaml

app = Flask(__name__)
db = yaml.load(open("endpoints/config.yaml"))
app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']
api = Api(app)
api.add_resource(User, '/api/v1/user/<string:username>', endpoint='get-user', methods=['GET'])
api.add_resource(User, '/api/v1/user/create', endpoint='create-user', methods=['POST'], resource_class_kwargs={'app': app})

if __name__ == '__main__':
    app.run(debug=True)
