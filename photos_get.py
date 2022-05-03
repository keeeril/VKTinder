import requests
from pprint import pprint

with open('/Users/keeeril/Desktop/Netology/Token/Token_user.txt', 'rt', encoding='utf-8') as file:
    token_user = file.readline()

def get_photo(ident):
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': ident,
        'album_id': 'profile',
        'access_token': token_user,
        'v': '5.131',
        'rev': '1',
        'extended': 1,
        'count': 3
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()['response']['items']
    photos = {}
    ss = 0
    for photo in response_outfit:
        like = photo['likes']['count']
        for size in photo['sizes']:
            if size['height'] > ss:
                photos[like] = size['url']
    sorted_photos = dict(sorted(photos.items()))
    return sorted_photos

