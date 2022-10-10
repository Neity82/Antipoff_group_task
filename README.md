# Antipoff_group_task
# Cервис на базе Django, который автоматизирует процесс поздравления сотрудников в чате в телеграмме

Каждый день проверяем в Списке сотрудников у кого сегодня ДР и отправляем рандомное сообщение с поздравлением из Списка поздравлений в групповой чат сотрудников от лица аккаунта руководителя

Ежедневно автоматически в 10.30 a.m. происходит поиск именинников и автоматическая отправка поздравлений в указанный вами чат.

## Предварительные требования
Для запуска вам необходимы следующие предварительные условия:

- Python 3.9
- Инструмент управления пакетами pip
- Проект Google Cloud
- Учетная запись Google
- API ID от Telegram API (https://tlgrm.ru/docs/api/obtaining_api_id)


## Настройки:

1. Клонируйте репозиторий

2. Создайте и активируйте виртуальное окружение:

`source venv/bin/activate`

3. Установите пакеты из requirements.txt:

`pip install -p requirements.txt`

4. Сделайте миграцию приложения:

`./mailing/python manage.py migrate`

5. Сохраните данные, полученные при Авторизация учетных данных на Google Sheets в файл google-config.json

6. Создайте файл `.env` и создайте в нем переменные:
   ```
    API_ID=api id (Telegram API)
    API_HASH=api hash (Telegram API)
    BOT_URL=https://api.telegram.org/bot
    CHAT_ID=id чата (в формате @idchat)
    PHONE=Номер телефона отправителя (в формате +XXXXXXXXXXX)
    GOOGLE_CONFIG=google-config.json (индентификатор клиента для работы с google sheets) 
    GOOGLE_EMPLOYEE_TABLE=Название таблицы с сотрудиками  (формат: Имя, Фамилия, Дата рождения)
    GOOGLE_TEXT_TABLE=Название таблицы с текстами поздравлений
   ```

## Запуск приложения

`./mailing/python manage.py runserver`
`celery -A marketplace_app worker -l INFO -B`
