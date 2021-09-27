from flask_restful import Api
from app import app
from user import User

restServer = Api(app)
restServer.add_resource(User, "/api/v1.0/user")