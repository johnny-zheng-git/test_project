######################################
# Time:2020/02/07
# writer: ZWQ
######################################

from flask import Blueprint
from flask_restplus import Api
from .views import *

user_mold = Blueprint('user_mold', __name__)
api = Api(user_mold)

#注册路由
api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
# api.add_resource(AllUsers, '/users')
api.add_resource(SecretResource, '/secret')