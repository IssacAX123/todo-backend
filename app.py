from flask import Flask
from flask_restful import Api
from endpoints.User import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/api/v1/user/<string:username>', endpoint='get-user', methods=['GET'])
api.add_resource(User, '/api/v1/user/create', endpoint='create-user', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
