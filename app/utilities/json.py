def get(json, atributo):
    try:
        return json[atributo]

    except Exception:
        return None


def get_or_error(json, attribute):
    try:
        return json[attribute]

    except Exception:
        raise Exception(f"{attribute} is missing.")
