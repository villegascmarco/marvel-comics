from flask import Blueprint, jsonify, request
from . import controller

users_route = Blueprint('users_route', __name__, url_prefix='/users')


@users_route.route('/add', methods=['POST'])
def add():
    output = {}
    try:
        output['action'], output['result'] = controller.add(request)
    except Exception as error:
        output['error'] = True
        output['message'] = str(error)
    return jsonify(output)


@users_route.route('/login', methods=['POST'])
def login():
    output = {}
    try:
        output['action'], output['result'] = controller.login(request)
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
