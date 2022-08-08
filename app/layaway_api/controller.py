from app.marvel_api.controller import search_comic_id
from app.users_api.controller import find_by_id
from app.layaway_api.database import Database
from app.utilities.json import get_or_error
from bson.json_util import dumps
import time


def add_to_layaway(current_user, request):
    comics_to_add = get_or_error(request.json, 'comics_to_add')

    data = []
    ts = time.time()
    for comic_id in comics_to_add:
        try:
            comic = search_comic_id(comic_id)[0]
            comic['laway_added_at'] = ts
            data.append(comic)
        except Exception:
            raise Exception(
                f'Comic with id {comic_id} does not exist. Only existing data in Marvel page is permited. Nothing was updated.')
    db = Database()

    if db.read({"user_id": current_user}):
        # Update
        db.update({"user_id": current_user},
                  {'$push': {'comics': {'$each': data}}})
        action = 'User info updated succesfully.'
    else:
        # Create
        db.write({"user_id": current_user, "comics": data})
        action = 'User info saved succesfully.'

    output = db.read({"user_id": current_user})
    user = find_by_id(output['user_id'])
    user.pop('password', None)
    output['user'] = user
    output.pop('user_id', None)

    return action, dumps(output)
