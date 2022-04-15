import requests
# from main import parametr

parametr = {
    'access_token': '3ff8b319bfca23cad51b27192c8f4a6a80657da721df1392ba003489a31043f857027c21864285dfd82ab',
    'v': '5.131',
    'city': 2,
    'age_from': 18,

    'sex': 1,
    'status': 6,
    'has_photo': 1
}

def find_users():
    url = 'https://api.vk.com/method/users.search'
    params = parametr
    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items']
print(find_users())
