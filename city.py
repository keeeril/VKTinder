import requests
import json

def get_city():
    url = 'https://api.vk.com/method/database.getCities'
    params = {
        'country_id': 1,
        'access_token': '3ff8b319bfca23cad51b27192c8f4a6a80657da721df1392ba003489a31043f857027c21864285dfd82ab',
        'v': '5.131',
        'need_all': 0,
        'count': 1000
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items']

