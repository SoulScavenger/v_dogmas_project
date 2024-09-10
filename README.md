
# Проект I_DOGMA(1из5)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# Описание:
Проект сделан мной для себя. Представляет собой площадку для размещения постов с командами, которые я использую при программирование, но могу забыть и дабы не гуглить, я использую данный сайт.

# Функционал:
- Регистрация;
- Создание постов (только для зарегистрированных пользователей);
- Редактирование постов из БД (только для автора поста);
- Удаление постов из БД (только для автора поста).


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
