from functools import wraps
from flask import request, jsonify, current_app
from app.users_api.controller import find_by_id
from bson.objectid import ObjectId
import datetime
import jwt


def validate_access():
    def inner_decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            token = None

            if 'Token' in request.headers:
                token = request.headers['Token']

            if not token:
                return jsonify({
                    "error": True,
                    "message": "Token not found."
                })

            try:
                jwt_data = jwt.decode(
                    token, 'kjasdfkjlsadkjfñlskajd', algorithms=["HS256"])

                expires_at = datetime.datetime.strptime(
                    jwt_data["expires_at"], '%Y-%m-%d %H:%M:%S.%f')

                if datetime.datetime.now() > expires_at:
                    return jsonify({
                        "error": True,
                        "message": "Token expired."
                    })

                user = find_by_id(ObjectId(jwt_data["id"]))

                if not user:
                    return jsonify({
                        "error": True,
                        "message": "User not found."
                    })

                return func(user["_id"], *args, **kwargs)

            except Exception as e:
                return jsonify({
                    "error": True,
                    "message": str(e)
                })
        return wrapped
    return inner_decorator
