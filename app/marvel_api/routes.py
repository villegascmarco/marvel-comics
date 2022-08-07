from flask import Blueprint, jsonify, request
from . import controller

marvel_route = Blueprint('marvel_route', __name__, url_prefix='/searchComics')


@marvel_route.route('/', methods=['POST'])
def index():
    output = {}
    try:
        output['result'] = controller.search(request)
    except Exception as error:
        output['error'] = True
        output['message'] = str(error)
    return jsonify(output)


# from textwrap import indent
# from connector import Connector
# from flask import Blueprint, jsonify, request
# from bson.json_util import dumps

# marvel_route = Blueprint('marvel_route', __name__, url_prefix='/marvel')


# @marvel_route.route('/searchComics', methods=['POST'])
# def index():
#     user_ip = request.remote_addr

#     return jsonify({
#         "a": user_ip
#     })


# @marvel_route.route('list', methods=['GET'])
# def list():
#     obj = Connector(request.json)
#     return jsonify({
#         'response': dumps(obj.read(), indent=2)
#     })


# @marvel_route.route('create', methods=['POST'])
# def create():
#     print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#     print(request.json)
#     print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
#     obj = Connector(request.json)
#     return jsonify({
#         'response': obj.write(request.json)
#     })
