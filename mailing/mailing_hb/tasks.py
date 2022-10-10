import asyncio
import random
from datetime import datetime
from typing import List

from telethon import TelegramClient

from mailing.celery import app
from mailing.settings import API_ID, API_HASH, PHONE, CHAT_ID
from mailing_hb.google_table import get_employee, get_text


def get_random_text(texts: List[str]) -> str:
    """
    Выбираем случайное поздравление из списка
    :param messages: Список поздравлений
    :return: Текст поздравления
    """

    i_message = random.randint(0, len(texts) - 1)
    text = texts[i_message]
    return text


@app.task
def send_messages():
    """
        Создаем Телеграм Клиента и отправляем сообщения в общий чат с поздравлением.
        Поздравление выбирается случайно из списка поздравлений для каждого клиента
        :param employees: Список словарей с данными сотрудников(Ф., И. и дата рождения)
        :param messages: Список поздравлений
        :return:
    """

    date_now = datetime.now().date().strftime("%d.%m")
    employees = get_employee()
    texts = get_text()

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
            text = get_random_text(texts=texts)
            message = f"{name} {nickname}, {text}"

            client.send_message(CHAT_ID, message)
    client.disconnect()
