import requests
from pprint import pprint

with open('/Users/keeeril/Desktop/Netology/Token/Token_user.txt', 'rt', encoding='utf-8') as file:
    token_user = file.readline()

def get_photo(ident):
    url = 'https://api.vk.com/method/photos.get'
    params = {
        'owner_id': ident,
        'album_id': 'wall',
        'access_token': token_user,
        'v': '5.131',
        'rev': '1',
        'extended': 1,
        'count': 3
    }

    response = requests.get(url, params=params)
    response_outfit = response.json()
    return response_outfit['response']['items']
#
pprint(get_photo(1))

# s = 0
# size = get_photo(1)[0]['sizes']
# for ii in size:
#     print(ii)
# #     if ii['height'] > s:
# #         s = ii['height']
# #         print(s)
#
# like = get_photo(1)[0]
# for qq in like['likes']:
#
# for i in get_photo(1):
#     print(i['likes']['count'])

photo = {}
like = 0
s = 0
for q in get_photo(1):
    # if q['likes']['count'] > like:
    like = q['likes']['count']
    for zz in q['sizes']:
        if zz['height'] > s:
            s = zz['height']
            url = zz['url']
            photo[like] = url
    print(photo[like])
