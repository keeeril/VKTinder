from random import randrange
from city import get_city
from photos_get import get_photo
import requests

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

with open('/Users/keeeril/Desktop/Netology/Token/Token_group.txt', 'rt', encoding='utf-8') as file:
    token_group = file.readline()

with open('/Users/keeeril/Desktop/Netology/Token/Token_user.txt', 'rt', encoding='utf-8') as file:
    token_user = file.readline()

vk = vk_api.VkApi(token=token_group)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

parametr = {
    'access_token': token_user,
    'v': '5.131',
    'has_photo': 1,
    'count': 1000
}

sexx = {
    1: 'женский',
    2: 'мужской',
    3: 'любой'
    }

family_status = {
    1: 'холост',
    2: 'встречается',
    3: 'помолвлен',
    4: 'женат',
    5: 'всё сложно',
    6: 'в активном поиске',
    7: 'влюблен',
    8: 'в гражданском браке'
}

def find_users():
    url = 'https://api.vk.com/method/users.search'
    response = requests.get(url, params=parametr)
    response_outfit = response.json()
    return response_outfit['response']['items']

count = 0
i = 1
photo = {}
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            request = event.text.lower()
            user_id = event.user_id
            user = vk.method('users.get', {'user_ids': user_id})

            if request == "привет":
                count = 0
                write_msg(user_id, f"Хай, {user[0]['first_name']}, в каком городе ищем?")

            if count == 1:
                parametr['city'] = get_city(request)['id']
                write_msg(user_id, "Возраст от:")

            elif count == 2:
                parametr['age_from'] = request
                write_msg(user_id, "Возраст до:")

            elif count == 3:
                parametr['age_to'] = request
                write_msg(user_id, "Какой пол?")

            for sex_noemr, sex in sexx.items():
                if request == sex:
                    parametr['sex'] = sex_noemr
                    write_msg(user_id, "Какое семейное положение?")

            for status_nomer, status in family_status.items():
                if request == status:
                    parametr['status'] = status_nomer
                    write_msg(user_id, "Отлично! Показываем?)")

            if request == 'да':
                idd = find_users()[i]['id']
                like = 0
                s = 0
                for q in get_photo(idd):
                    # if q['likes']['count'] > like:
                    like = q['likes']['count']
                    for zz in q['sizes']:
                        if zz['height'] > s:
                            s = zz['height']
                            url = zz['url']
                            photo[like] = url
                    write_msg(user_id, f"{url}")
                write_msg(user_id, f"https://vk.com/id{idd}")

            elif request == 'дальше':
                idd = find_users()[i]['id']
                like = 0
                s = 0
                for q in get_photo(idd):
                    like = q['likes']['count']
                    for zz in q['sizes']:
                        if zz['height'] > s:
                            s = zz['height']
                            url = zz['url']
                            photo[like] = url
                    write_msg(user_id, f"{photo[like]}")
                write_msg(user_id, f"https://vk.com/id{idd}")

            count += 1
            i += 1
