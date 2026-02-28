# Тестовое задание: Django 5.2 + MySQL + Bootstrap 5 + Slick Slider + django-filer + sortable2

Данный проект собирает страницу с галереей (Bootstrap 5 + Slick Slider, полноэкранная галерея slick-lightbox).
Изображения и порядок слайдов управляются через админку (django-filer, django-admin-sortable2).
Интерфейс локализован на русский.

## Стек

- Python 3.12
- Django 5.2
- MySQL (mysqlclient)
- django-filer, easy-thumbnails
- django-admin-sortable2
- Bootstrap 5, Slick Slider (Slider Syncing), slick-lightbox

## **Быстрый старт**

- Подготовьте БД MySQL:

```
CREATE DATABASE test_task CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'test_user'@'%' IDENTIFIED BY 'test_password';
GRANT ALL PRIVILEGES ON test_task.* TO 'test_user'@'%';
FLUSH PRIVILEGES;
```

- Виртуальное окружение и зависимости:

```python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r req.pip
```

- Миграции и запуск:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- Админка: http://127.0.0.1:8000/admin/
- Главная: http://127.0.0.1:8000/

## **Работа со слайдами**

- В админке создайте «Слайды»: загрузите изображение через django-filer, отметьте «Активный».
- Порядок можно менять drag&drop (django-admin-sortable2).

## **Заметки**

- Для сборки mysqlclient нужны dev-заголовки:
  - Ubuntu/Debian: `sudo apt-get install libmysqlclient-dev python3.12-dev build-essential`
  - macOS: `brew install mysql pkg-config`