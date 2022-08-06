from flask import Flask
from routes.marvel_route import marvel_route


if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(marvel_route)
    app.run(debug=True, host='0.0.0.0')
