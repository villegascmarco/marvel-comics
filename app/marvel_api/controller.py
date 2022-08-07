from decouple import config
import time
import hashlib
import requests

API_URL = 'https://gateway.marvel.com:443/v1/public/'


def search(request):
    if not request.json:
        raise TypeError(f'Excpected JSON, but ${type(request)} was found.')
    data = request.json

    type = get(data, 'type')

    if type == None:
        # Return all character order by name
        return __list_all_characters()
    elif type.lower() not in ['character', 'comic']:
        raise Exception(
            f'"{type}" is not a valid option, please select either "character" or "comic"')

    return data


def __list_all_characters():
    public_key = __get_public_key()
    ts = str(time.time())
    hash = __get_hash(public_key, ts)

    response = requests.get(
        f'{API_URL}characters?orderBy=name&ts={ts}&apikey={public_key}&hash={hash}')

    if response.status_code != 200:
        raise Exception(response.json())

    results = response.json()['data']['results']

    characters = [
        {"id": character['id'],
         "name": character['name'],
         "image": character['thumbnail']['path']+'.jpg',
         "appearances":character['comics']['available']} for character in results]
    return characters


def get(json, atributo):
    try:
        return json[atributo]

    except Exception:
        return None


def __get_public_key():
    public_key = config('PUBLIC_KEY')

    if type(public_key) == None:
        raise Exception("Public key not found.")

    return public_key


def __get_hash(public_key, timestamp):
    # Assume public_key and timestamp ar not null due to current workflow
    private_key = config('PRIVATE_KEY')
    if type(private_key) == None:
        raise Exception("Private key not found.")

    str_enconded = (timestamp+private_key+public_key).encode()
    api_key = hashlib.md5(str_enconded)
    return api_key.hexdigest()
