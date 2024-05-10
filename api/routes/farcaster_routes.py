from flask import Blueprint, request, jsonify

farcaster_routes = Blueprint("farcaster_routes", __name__)


@farcaster_routes.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}, 200

