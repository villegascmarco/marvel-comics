from app.users_api.controller import find_by_id
from app.layaway_api.database import Database
from app.utilities.json import get_or_error
from bson.json_util import dumps
from operator import attrgetter
from collections import OrderedDict


def get_layaways_user(current_user, request):

    field_target = get_or_error(request.json, 'field_target')
    order_by = get_or_error(request.json, 'order_by').lower()

    if order_by not in ['asc', 'desc']:
        raise Exception('Only "asc" "desc" values are accepted as order_by.')

    db = Database()

    output = db.read({"user_id": current_user})

    if not output:
        return "Listing related data.", "No related record has found."

    user = find_by_id(output['user_id'])
    user.pop('password', None)
    output['user'] = user
    output.pop('user_id', None)

    try:
        # Sort
        output['comics'].sort(key=lambda x: x[field_target],
                              reverse=(True if order_by == 'desc' else False))
    except Exception:
        raise Exception(f'Invalid field has found "{field_target}".')
    return "Listing related data.", dumps(output)
