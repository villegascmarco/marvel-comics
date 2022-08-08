from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .marvel_api.routes import marvel_route
        from .users_api.routes import users_route
        from app.layaway_api.routes import layaway_route
        from app.layaway_list_api.routes import layaway_list_route

        app.register_blueprint(marvel_route)
        app.register_blueprint(users_route)
        app.register_blueprint(layaway_route)
        app.register_blueprint(layaway_list_route)
        return app
