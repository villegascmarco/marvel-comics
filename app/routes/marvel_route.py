from flask import Blueprint, jsonify, request

marvel_route = Blueprint('marvel_route', __name__, url_prefix='/marvel')


@marvel_route.route('/', methods=['POST'])
def index():
    user_ip = request.remote_addr

    return jsonify({
        "user_ipa": user_ip
    })
