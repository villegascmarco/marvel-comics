from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .marvel_api.routes import marvel_route
        app.register_blueprint(marvel_route)
        return app
