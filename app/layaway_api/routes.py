from flask import Blueprint, jsonify, request
from app.layaway_api import decorator as session
from . import controller

layaway_route = Blueprint('layaway_route', __name__,
                          url_prefix='/addToLayaway')


@layaway_route.route('/', methods=['POST'])
@session.validate_access()
def add(current_user):
    output = {}
    try:
        output['action'], output['result'] = controller.add_to_layaway(
            current_user, request)
    except Exception as error:
        output['error'] = True
        output['message'] = str(error)
    return jsonify(output)
