from flask import Blueprint, jsonify, request
from . import controller

marvel_route = Blueprint('marvel_route', __name__, url_prefix='/searchComics')


@marvel_route.route('/', methods=['POST'])
def index():
    output = {}
    try:
        output['action'], output['result'] = controller.search(request)
    except Exception as error:
        output['error'] = True
        output['message'] = str(error)
    return jsonify(output)
