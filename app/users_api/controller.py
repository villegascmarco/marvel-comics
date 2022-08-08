from werkzeug.security import generate_password_hash, check_password_hash
from app.users_api.database import Database
from bson.json_util import dumps
from app.utilities import json
import datetime
import jwt


def add(request):
    data = request.json

    email = json.get_or_error(data, 'email')
    json.get_or_error(data, 'password')

    db = Database()

    if db.read({"email": email}) != None:
        raise Exception("Email already in use")

    data['password'] = generate_password_hash(
        data['password'], method='sha256')

    return 'User created.', db.write(data)


def login(request):
    data = request.json

    email = json.get_or_error(data, 'email')
    password = json.get_or_error(data, 'password')

    db = Database()

    user_db = db.read({"email": email})

    if not user_db or not check_password_hash(user_db['password'], password):
        return 'Not logged in.', 'Password or email are incorrect.'
    expires_at = str(datetime.datetime.utcnow() +
                     datetime.timedelta(minutes=60*24*10))
    token = jwt.encode(
        {'id': str(user_db['_id']), "expires_at": expires_at}, 'kjasdfkjlsadkjfñlskajd')
    user_db.pop('password', None)
    user_db.pop('_id', None)
    user_db['token'] = token

    return 'Logged on succesfully.', dumps(user_db)

