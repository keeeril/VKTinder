from random import randrange
from photos_get import get_photo
import requests
import sqlalchemy
from package.token import token, token_group

engine = sqlalchemy.create_engine('postgresql://kirill:123456@localhost:5432/kirill_database')
connection = engine.connect()

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_api.VkApi(token=token_group)
longpoll = VkLongPoll(vk)

parametr = {
    'access_token': token,
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


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

count = 0
i = 0
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
                parametr['hometown'] = request
                write_msg(user_id, "Возраст от:")

            elif count == 2:
                parametr['age_from'] = request
                write_msg(user_id, "Возраст до:")

            elif count == 3 and request > parametr['age_from']:
                parametr['age_to'] = request
                write_msg(user_id, "Какой пол?")

            for sex_noemr, sex in sexx.items():
                if request == sex:
                    parametr['sex'] = sex_noemr
                    write_msg(user_id, "Какое семейное положение? (холост,встречается,помолвлен,женат,\n"
                                       "всё сложно,в активном поиске,влюблен,в гражданском браке)")

            for status_nomer, status in family_status.items():
                if request == status:
                    parametr['status'] = status_nomer
                    write_msg(user_id, "Отлично! Показываем?)")

            if request == 'да':
                idd = find_users()[i]['id']
                for url in get_photo(idd).values():
                    write_msg(user_id, f"{url}")
                write_msg(user_id, f"https://vk.com/id{idd}")
                write_msg(user_id, f"Если хотите продолжить поиск введите 'Дальше'")
                sel_user = connection.execute("""SELECT * FROM users;""").fetchall()
                user = f"https://vk.com/id{idd}"
                for us in sel_user:
                    if user != us[1]:
                        connection.execute(f"INSERT INTO users(id_users) VALUES ('{user}')")

            elif request == 'дальше':
                idd = find_users()[i]['id']
                for url in get_photo(idd).values():
                    write_msg(user_id, f"{url}")
                write_msg(user_id, f"https://vk.com/id{idd}")
                sel_user = connection.execute("""SELECT * FROM users;""").fetchall()
                user = f"https://vk.com/id{idd}"
                for us in sel_user:
                    if user != us[1]:
                        connection.execute(f"INSERT INTO users(id_users) VALUES ('{user}')")
            count += 1
            i += 1
