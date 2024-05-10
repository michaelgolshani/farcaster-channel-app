from flask import Blueprint, request, jsonify
import requests
import os

farcaster_routes = Blueprint("farcaster_routes", __name__)


@farcaster_routes.route("/ping", methods=["GET"])
def ping():
    return {"message": "pong"}, 200


# create a path that will save the trending channels in the farcaster database to our database
@farcaster_routes.route('/trending_channels', methods=['GET'])
def get_trending_channels():
    """Get the trending channels from the farcaster database and save them to our database"""

    URL = "https://api.neynar.com/v2/farcaster/channel/list?limit=50"
    API_KEY = os.environ.get("NEYNAR_API_KEY")
    headers = {
        "accept": "application/json",
        "api_key": f'{API_KEY}'
    }

    response = requests.get(URL, headers=headers, timeout=5)

    if response.status_code == 200:
        data = response.json()
        return data, 200
    else:
        return {"message": "Unable to get trending channels"}, 500




