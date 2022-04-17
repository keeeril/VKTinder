import requests

def get_photo(ident):
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': ident,
        'album_id': 'wall',
        'access_token': '427a7e0613e5ce3ed287a07d9e293dc20bb14ed38283cad05f42ab7d72021e819832d07b9c317b650f219',
        'v': '5.131',
        'rev': '1',
        'extended': 1
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items']
