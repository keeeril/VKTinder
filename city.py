import requests
import json

with open('/Users/keeeril/Desktop/Netology/Token/Token_user.txt', 'rt', encoding='utf-8') as file:
    token_user = file.readline()

def get_city(q):
    url = 'https://api.vk.com/method/database.getCities'
    params = {
        'country_id': 1,
        'q': q,
        'access_token': token_user,
        'v': '5.131',
        'need_all': 0,
        'count': 1000
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items'][0]
