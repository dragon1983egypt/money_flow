# Project Title😎
Описание:
ДДС (движение денежных средств) — это процесс учета, управления и анализа
поступлений и списаний денежных средств компании или частного лица. В рамках
данного задания пользователь должен иметь возможность вести учет всех денежных
операций с учетом следующих параметров.
====================================================================================
Веб-приложение, которое позволяет пользователям
создавать, редактировать, удалять и просматривать записи о движении денежных
средств.Веб-приложение  удобно, имеeт интуитивно понятный
интерфейс и обеспечивает соблюдение логических зависимостей между сущностями.
====================================================================================
## Table of Contents😉
Записи о движении денежных средств
Поля(fields): дата, статус, тип, категория, подкатегория, сумма, комментарий.
автоматическое и рцчное заполнение даты
фильтрация по дате, статусу, типу, категории, подкатегории
Поля обязательные в таблице:Поля: сумма, тип, категория, подкатегория.
редкатирование, удаление, создание записи в приложении
=================================================================
Справочники:✌
Статусы(бизнес)
Типы(пополнение)
подкатегории(связка с типом)
категории(связка с категорией)
===============================================================
Зависимости:
Категория не может быть выбрана, если она не соответствует выбранному типу
Подкатегория не может быть выбрана, если она не соответствует выбранной категории.
=======================================================================
Валидация😎
На сервере (Django)
тип, категория, подкатегория, сумма.
======================================================================
## Installation and start proect✔✔✔✔
1. клон репозитория 
git clone https://github.com/dragon1983egypt/money_flow.git
2. Устанавливаем виртуальное окружение python -m venv venv  и активвируем его venv\Scripts\activate
3. pip install -r requirements.txt устанавлиываем зависимости для приложения 
4. db.sqlite3 база данных настраивается автоматически, для настройки Postqresql устанавливаем pgadmin4 и регистрируемся и заходим в настройки settings в database меняем параметры ( 'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'name',
        'USER':  'name',
        'PASSWORD': '#####',
        'HOST': 'localhost',
        'PORT': '5432', )
5. Применяем миграции python manage.py migrate
6. Делаем миграции python manage.py makemigrations
7. заходим в настройки и меняем некоторые параметры в TEMPLATES 'DIRS': [BASE_DIR/'main'/'templates'], LANGUAGE_CODE = 'ru-ru' приложение можно полностью русифицировать (админ панель - через  verbose_name или в settings указать  LOCALE_PATHS = (os.path.join(BASE_DIR, 'translations', 'locale'),) через генерацию файла ./manage.py makemessages -a  и  ./manage.py compilemessages)
8. Затем создаем суперпользователя (админа)
Для входа в админ панель: python manage.py createsuperuser
указываем имя, пароль, почту 
9. http://127.0.0.1:8000/admin/ адрес для входа в админку можно дополнительно создать страницу админ панель
10. Запуск приложения python manage.py runserver
11. http://127.0.0.1:8000/ адрес
12.P/S  Приложение создано на джанго с созданием forms, admins, views, gitignore, git, launch.json, apps, models, urls, requirements, readme, 
templates(
    base.html ****
) для красоты приложения можно использовать bootstrap, javascript, css 
13. Screenshots project:(расширение файлов png)👀

удаление транзакции: delete transaction
создание транзакции: add transaction
фильтрация: filters and transaction
первый запуск админ панели: first launch admin
запуск сервера: launch server
админка: админ панель
главный экран приложения cash_flow
запись создана: создание записи
справочники: справочники
удаление записи: удаление записи
редактирование статуса, транзакции и т.д.: радактирование записи, транзакции, статуса
добавление статуса, тип: дабление статуса


Дополнительно добавил в приложение DEBUG режим , в settings STATIC_ROOT для переноса приложения на сервер.
Перевел проект на бд postqresql добавил русские наименования в админке приложения. НЕ много добавил футер. Добавил файлы в requirements.txt добавил скрины приложения

Устанавливаем pgadmin 4 (postqresql)
Создаем новую базу данных cash_flow и пользователя  dimasin20831 меняем настройки и делаем его админом .затем заходим в settings в databases меняем настройки для подключения 
Устанавливаем psycorpg 2 для работы с postgresql
Либо удаляем либо оставляем dbsqlite3  дополнительно
Применяем мингграции к проекту python manage.py makemigrations
python manage.py migrate
создаем superuser 

