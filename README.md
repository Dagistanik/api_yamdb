## Работа с Git. Командный проект YaMDb api.

### Описание
Проект собирает отзывы пользователей на произведения. Произведения делятся на категории. Произведению может быть присвоен жанр. Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг.

#### Инструкция по развёртыванию
* Клонировать репозиторий и перейти в него в командной строке:
```python
git clone https://github.com/Dagistanik/api_yamdb.git
```
```python
cd api_yamdb
```
* Cоздать и активировать виртуальное окружение:
```python
python -m venv env
```
```python
source venv/Scripts/activate
```
* Установить зависимости из файла requirements.txt
```python
python -m pip install --upgrade pip
```
```python
pip install -r requirements.txt
```
* Запустить сервер
```python
python manage.py runserver
```
#### Язык

* Python 3.7

#### Стек технологий

* Python 3
* ООП
* Django
* Django REST Framework
* PostgreSQL
* Git 
* Pytest

### Создатели проекта
* PVchuchkov
* Dagistanik 
* Ramlog-JJ