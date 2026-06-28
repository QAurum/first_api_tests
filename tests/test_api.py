import requests # requests — это библиотека, которая отправляет запросы
import pytest
import json

''' НАЗВАНИЯ
test_get_user_by_id
test_create_post
test_update_user_data

ЗАПУСК
pytest -v — подробно
pytest -k "test_get" — запустить только тесты с "test_get" в названии
pytest -x — ост
'''

 # Функция открывает файл и с помощью json.load() превращает его содержимое в словарь Python
def load_config():

    with open("config/config.json", "r") as f:  # открываем файл для чтения
        return json.load(f)  # читаем и преобразуем JSON в словарь
        
config = load_config() #это вызов функции, которая возвращает словарь с настройками. Переменная config теперь хранит этот словарь
base_url = config["base_url"] #это обращение к словарю по ключу "base_url", чтобы получить значение базового URL

def test_get_post(): # get — это HTTP-метод (мы отправляем GET-запрос), а post — это ресурс (мы запрашиваем конкретный пост, /posts/1)

    # 1. Отправляем GET-запрос на фейковый API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # 2. Проверяем, что сервер ответил (статус код 200)
    assert response.status_code == 200
    
    # 3. Проверяем, что в ответе есть нужное поле
    data = response.json() # Это метод, который преобразует тело ответа (которое приходит в формате JSON) в словарь Python. data становится словарём, к которому можно обращаться по ключам: data["id"], data["title"] и т.д.
    assert data["id"] == 1
    

#POST-запрос на создание поста:
def test_post_create_post():
    url = f"{base_url}/posts"
    # Это способ передать серверу данные в формате JSON:
    payload = {"title": "The call of Cthulhu", "body": "Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn", "userId": 1}
    # Параметр json= автоматически преобразует переданный словарь (payload) в JSON-строку и устанавливает правильный заголовок Content-Type: application/json
    requests = requests.post(url, json=payload)
    data = response.json()
    assert response.status_code == 201
    assert isinstance(data["id"], int)


Залей код на GitHub и добавь простой README.md с описанием проекта (это будет твоё портфолио).

GitHub Actions — настрой автоматический запуск тестов при каждом push. Это покажет, что ты умеешь работать с CI/CD.
'''
