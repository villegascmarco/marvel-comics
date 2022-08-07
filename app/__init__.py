from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .marvel_api.routes import marvel_route
        from .users_api.routes import users_route

        app.register_blueprint(marvel_route)
        app.register_blueprint(users_route)
        return app
