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
