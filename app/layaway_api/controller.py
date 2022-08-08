from bson.json_util import dumps


def add_to_layaway(current_user, request):
    return "", dumps(current_user)
