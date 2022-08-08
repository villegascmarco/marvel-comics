from flask import Blueprint, jsonify, request
from app.layaway_api import decorator as session
from . import controller

layaway_list_route = Blueprint('layaway_list_route', __name__,
                               url_prefix='/getLayawayList')


@layaway_list_route.route('/', methods=['POST'])
@session.validate_access()
def index(current_user):
    output = {}
    try:
        output['action'], output['result'] = controller.get_layaways_user(
            current_user, request)
    except Exception as error:
        output['error'] = True
        output['message'] = str(error)
    return jsonify(output)
