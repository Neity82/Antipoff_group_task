import random

import requests
import gspread
from telethon import TelegramClient, sync, events
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from mailing.settings import CHAT_ID, BOT_URL, BOT_TOKEN
from mailing_hb.google_table import get_employee, get_text
from mailing_hb.telegram import send_message


class Index(TemplateView):
    template_name = 'mailing_hb/index.html'

    def post(self, request):
        # api_id = 18323783
        # api_hash = '08545c9a06783c79008c439519ac9cbb'
        # token = BOT_TOKEN
        phone = '79215389696'

        employees = get_employee()
        messages = get_text()

        send_message(employees=employees, messages=messages)

        # url = f"{BOT_URL}{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={nickname}, Hello"
        # print(requests.get(url).content)

        # client = TelegramClient('session', api_id, api_hash)
        # client.connect()
        # print(client.get_me())
        # client.send_message("@FamilyTyzov", "Hello")
        # # if not client.is_user_authorized():
        # #     client.send_code_request(phone)
        # #     client.sign_in(phone, input('Enter the code: '))
        # #
        # # try:
        # #     receiver = InputPeerUser('user_id', 'user_hash')
        # #     client.send_message(receiver, message, parse_mode='html')
        # # except Exception as e:
        # #     print("!!!!!!!!!!!", e)
        #
        # client.disconnect()



        return HttpResponseRedirect(reverse('index'))
