from flask import Blueprint


hello_world_routes = Blueprint("hello_world_routes", __name__)


@hello_world_routes.route("/")
def hello_world():
    return {"message": "Hello, World TEST3!"}, 200
