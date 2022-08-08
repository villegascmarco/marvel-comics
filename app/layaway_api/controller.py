from app.marvel_api.controller import search_comic_id
from app.layaway_api.database import Database
from app.utilities.json import get_or_error
from bson.objectid import ObjectId
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
    # return "", dumps(data)
    if db.read({"user_id": current_user}):
        # Update
        output = db.update({"user_id": current_user},
                           {'$push': {'comics': {'$each': data}}})
        return 'User info updated succesfully', dumps(output)
    else:
        # Create
        output = db.write({"user_id": current_user, "comics": data})
        return "User info saved succesfully.", dumps(output)


def get_layaways_user(curren_user, request):
    pass
