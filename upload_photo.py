from random import randrange
from city import get_city
from photos_get import get_photo
import requests
with open('/Users/keeeril/Desktop/Netology/Token/Token_group.txt', 'rt', encoding='utf-8') as file:
    token_group = file.readline()

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = token_group

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

vk.method("messages.send", {"peer_id": 8012266, "message": "TEST", "attachment": "photo-57846937_457307562", "random_id": 0})

