import asyncio
from datetime import datetime
import random
from typing import List, Dict

import requests
from telethon import TelegramClient

from mailing.settings import BOT_URL, BOT_TOKEN, CHAT_ID, API_ID, API_HASH, PHONE


def get_text(texts: List[str]) -> str:
    """
    Выбираем случайное поздравление из списка
    :param messages: Список поздравлений
    :return: Текст поздравления
    """

    i_message = random.randint(0, len(texts) - 1)
    text = texts[i_message]
    return text


def send_message(employees: List[Dict[str, str]], messages: List[str]):
    """
    Создаем Телеграм Клиента и отправляем сообщения в общий чат с поздравлением.
    Поздравление выбирается случайно из списка поздравлений для каждого клиента
    :param employees: Список словарей с данными сотрудников(Ф., И. и дата рождения)
    :param messages: Список поздравлений
    :return:
    """

    date_now = datetime.now().date().strftime("%d.%m")
    # url = f"{BOT_URL}{BOT_TOKEN}/sendMessage"

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    client = TelegramClient('messages_hb', API_ID, API_HASH, loop=loop)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(PHONE)
        client.sign_in(PHONE, input('Enter the code: '))

    for employee in employees:
        date_birth = datetime.strptime(employee["Дата рождения"], "%d.%m.%Y").strftime("%d.%m")

        if date_birth == date_now:
            nickname = employee["Telegram"]
            name = employee["Имя"]
            message = get_text(texts=messages)
            text = f"{name} {nickname}, {message}"

            client.send_message(CHAT_ID, text)

        # Отправка сообщений от имени бота
        #     params = {
        #         "chat_id": CHAT_ID,
        #         "text": f"{name} {nickname}, {message}"
        #     }
        #     requests.get(url=url, params=params)

    client.disconnect()

