from flask import Flask
from api.routes.hello_world_routes import hello_world_routes
from api.routes.farcaster_routes import farcaster_routes


app = Flask(__name__)


app.register_blueprint(farcaster_routes, url_prefix="/api/farcaster")
app.register_blueprint(hello_world_routes, url_prefix="/api/hello")


if __name__ == "__main__":
    app.run(debug=True)
