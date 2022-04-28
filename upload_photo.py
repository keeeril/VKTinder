from random import randrange
from city import get_city
from photos_get import get_photo
import requests

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'c3565f4fff3ad1de652be3bd3651ad015965d8bdb1cc64aa46b3cdadea269c798c99d202f90732e29a999'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

vk.method("messages.send", {"peer_id": 8012266, "message": "TEST", "attachment": "photo-57846937_457307562", "random_id": 0})

