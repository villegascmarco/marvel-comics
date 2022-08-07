from decouple import config
from ..utilities import json
import urllib.parse
import time
import hashlib
import requests

API_URL = 'https://gateway.marvel.com:443/v1/public/'


def search(request):
    if not request.json:
        raise TypeError(f'Excpected JSON, but ${type(request)} was found.')
    data = request.json

    type = json.get(data, 'type')

    if type == None:
        # Return all character order by name
        return 'Type was not found, listing all characters', __list_all_characters()
    elif type.lower() not in ['character', 'comic']:
        raise Exception(
            f'"{type}" is not a valid option, please select either "character" or "comic"')

    filter = json.get_or_error(data, 'filter')
    if type.lower() == 'character':
        return 'Searching characters', search_character(filter)

    return 'Searching comics', search_comic(filter)


def search_character(name):
    public_key, ts, hash = __get_api_auth()

    response = requests.get(
        f'{API_URL}characters?nameStartsWith={urllib.parse.quote(name)}&ts={ts}&apikey={public_key}&hash={hash}')
    if response.status_code != 200:
        raise Exception(response.json())

    results = response.json()['data']['results']

    characters = [
        {"id": character['id'],
         "name": character['name'],
         "image": character['thumbnail']['path']+'.jpg',
         "appearances":character['comics']['available']} for character in results]
    return characters


def search_comic(name):
    public_key, ts, hash = __get_api_auth()

    response = requests.get(
        f'{API_URL}comics?titleStartsWith={urllib.parse.quote(name)}&ts={ts}&apikey={public_key}&hash={hash}')
    if response.status_code != 200:
        raise Exception(response.json())

    results = response.json()['data']['results']

    comics = [
        {"id": comic['id'],
         "tittle": comic['title'],
         "image": comic['thumbnail']['path']+'.jpg',
         "onsaleDate":comic['dates'][0]['date']} for comic in results]
    return comics


def __list_all_characters():
    public_key, ts, hash = __get_api_auth()

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


def __get_api_auth():
    public_key = __get_public_key()
    ts = str(time.time())
    hash = __get_hash(public_key, ts)

    return public_key, ts, hash


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
