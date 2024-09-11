
# Проект I_DOGMA(1 из 5)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# Описание:
Проект сделан мной для себя. Представляет собой площадку для размещения постов с командами, которые я использую при программирование, но могу забыть и дабы не гуглить, я использую данный сайт.

# Функционал:
- Регистрация;
- Поиск;
- Создание постов (только для зарегистрированных пользователей);
- Редактирование постов из БД (только для автора поста);
- Удаление постов из БД (только для автора поста);
- Доступ к сайту через API;


# Запуск
- для запуска проекта необходимо установить пакеты из requirements.txt:  
```
pip install -r requirements.txt
```
- выполнить миграции
```
python manage.py migrate
```
- запуск проекта
```
python manage.py runserver
```
# Проект II_DOGMA(2 из 5)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# Описание:
Телеграм Бот для доступа к проекту I_DOGMA. Реализация через DRF/aiogram/asyncio.

# Функционал:
- /commands - отображение всех записей на сайте;
- /command 'id_command' - отображение конкретной записи;


# Запуск
- для запуска проекта необходимо установить пакеты из requirements.txt:  
```
pip install -r requirements.txt
```
- запуск проекта
```
python bot.py
```
- Токены для доступа к боту и сайту необходимо сделать свои...