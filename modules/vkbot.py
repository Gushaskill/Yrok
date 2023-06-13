#VK BOT
import random
from wiki import *
from course import *
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def get_wiki(article):
    pass


def getCourse(param):
    pass


def getCourse(param):
    pass


def getCourse(param):
    pass


def main():

    token = 'vk1.a.JxeiN-J_-60_Mo0FRktIRGNYHFOaykF4irOBlAGXx1rC3-dD3X76ImNyzltTqTFaiZO4FfTdtA_5spN91mxmwcWk-S7UIVy-DM0H_ghG5ZS5D8IUQkEfUjAdh9G4twtPzXhifal5ZI1YJDT046as6G7h-qvV_Rr250Oic1lHgSntQlPb8iEXl44BkrnzmKRitLAj-I_59lg6FMtxcepkpg'

    vk_session = vk_api.VkApi(token= token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            user_id = event.user_id
            random_id = random.randint(1, 1000000000)

            if msg == 'курс':
                response = "{0} рублей за 1 доллар\n" \
                           "{1} рублей за 1 фунт\n" \
                           "{2} рублей за 1 евро"
                response = response.format(getCourse("R01235"), getCourse("R01035"), getCourse("R01239"))
                vk.messages.send(user_id = event.user_id, random_id = random_id, message = response)
            elif msg[0:2] == "-в":
                article = msg[2:]
                response = get_wiki(article)
            else:
                response = "Неизвестная команда"
            vk.messages.send(user_id=event.user_id, random_id=random_id, message = response[0:4096])
                    


main()

