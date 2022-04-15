import requests

def get_photo(ident):
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': ident,
        'album_id': 'wall',
        'access_token': '3ff8b319bfca23cad51b27192c8f4a6a80657da721df1392ba003489a31043f857027c21864285dfd82ab',
        'v': '5.131',
        'rev': '1',
        'extended': 1
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items']
