from app.users_api.database import Database
from app.utilities import json
from werkzeug.security import generate_password_hash


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
