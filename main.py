from random import randrange
from city import get_city
import requests

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'c3565f4fff3ad1de652be3bd3651ad015965d8bdb1cc64aa46b3cdadea269c798c99d202f90732e29a999'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

parametr = {
    'access_token': '3ff8b319bfca23cad51b27192c8f4a6a80657da721df1392ba003489a31043f857027c21864285dfd82ab',
    'v': '5.131',
    'has_photo': 1
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
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            request = event.text
            user_id = event.user_id
            user = vk.method('users.get', {'user_ids': user_id})

            if request == "привет":
                write_msg(user_id, f"Хай, {user[0]['first_name']}, в каком городе ищем?")

            for city in get_city():
                if request == city['title']:
                    parametr['city'] = city['id']
                    write_msg(user_id, "Возраст от:")

            # for age_from in range(0, 100, 1):
            #     if request == str(age_from):
            #         parametr['age_from'] = age_from
            #         write_msg(user_id, "Возраст до:")

            for age_to in range(0, 100, 1):
                if request == str(age_to):
                    parametr['age_to'] = age_to
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

                # def find_users():
                #     url = 'https://api.vk.com/method/users.search'
                #     response = requests.get(url, params=parametr)
                #     response_outfit = response.json()
                #     return response_outfit['response']['items']
                for i in find_users():
                    write_msg(user_id, f"{i['id']}")
                    break
            elif request == 'дальше':
                count += 1
                for j in range(1, 1000):
                    if j == count:
                        write_msg(user_id, f"{find_users()[j]}")





