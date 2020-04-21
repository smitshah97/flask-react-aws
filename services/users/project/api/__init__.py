# services/users/project/api/__init__.py


from flask_restx import Api

from project.api.auth import auth_namespace
from project.api.ping import ping_namespace
from project.api.sample import sample_namespace
from project.api.users.views import users_namespace

api = Api(version="1.0", title="Users API", doc="/doc/")

api.add_namespace(sample_namespace, path="/sample")
api.add_namespace(ping_namespace, path="/message")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(auth_namespace, path="/auth")
