<h1 align="center">Django integration with Stripe</h1>
В данном проложение реализована оплата через сторонний сервис Stripe

## Стек технологий:
- python
- django
- djangorestframework
- psycopg2-binary
- stripe
- docker
- docker-compose

## Установка

**Инструкция по работе с Dockerfile и docker-compose**

Запуск проекта:
- Клонируем себе проект
- Устанавливаем виртуальное окружение с помощью команды: ***python -m venv env***<br>
- Активируем виртуальное окружение:
- для Windows с помощью команды: ***env\Scripts\activate***<br>
- для macOS и Linux с помощью команды: ***source env/bin/activate***<br>
- Собираем Docker образ с помощью команды:  ***docker-compose build***<br>
- Запустите контейнеры с помощью команды:  ***docker-compose up***<br>
- Миграции применяются автоматически<br>
- Пользователь и данные в базу подгружаются так же автоматически

Пользователь:<br>
username: admin<br>
password: 12345<br>