# Дипломный проект курса "Python-разработчик" от Яндекс.Практикумм Foodgram
![workflow](https://github.com/chumanastasia/foodgram-project-react/actions/workflows/workflow.yml/badge.svg)

# 🍱 🥗 🍜 Описание проекта Foodgram 🍱 🥗 🍜
Проект Foodgram позволяет пользователям публиковать рецепты, подписываться на публикации других авторов, добавлять понравившиеся рецепты в список «Избранное», а также скачивать список продуктов, необходимых для приготовления выбранных блюд.
Ccылка на проект: http://158.160.22.145/
# 💻 Стек технологий 💻
 - Python 3.8
 - Django 
 - Django REST Framework
 - PostgreSQL
 - Docker
 - Nginx
 - Gunicorn
 - GitHub Actions
 - Yandex.Cloud

# 🛠️⚙️ Запуск проекта на сервере 🛠️⚙️
- Установить Docker и Docker Compose
- Переместить файлы docker-compose.yml, nginx.conf на удаленный сервер
- Создать файл .env  и поместить туда следующие значения:
```commandline
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=ваш_секретный_ключ
DEBUG=False
```
В директории, где находится docker-compose.yml, выполнить команду:
```commandline
docker-compose up -d --build
```
- После запуска контейнеров выполнить миграции:
```commandline
docker-compose exec backend python manage.py migrate
```
- Создать суперпользователя:
```commandline
docker-compose exec backend python manage.py createsuperuser
```
- Собрать статику:
```commandline
docker-compose exec backend python manage.py collectstatic --noinput
```
- Загрузить ингредиенты:
```commandline
docker-compose exec backend python manage.py loaddata ingredients.json
```
Теперь проект доступен по адресу http://<ваш_IP_адрес>/ 