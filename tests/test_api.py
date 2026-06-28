import requests # requests — это библиотека, которая отправляет запросы
import pytest

''' НАЗВАНИЯ
Название должно отражать что ты тестируешь, а не как.

test_get_user_by_id
test_create_post
test_update_user_data

ЗАПУСК
Ты запустила тесты с -v (verbose) — это правильно. Это показывает подробный вывод. Другие полезные опции:

pytest -v — подробно

pytest -k "test_get" — запустить только тесты с "test_get" в названии

pytest -x — ост
'''


def test_get_post(): # get — это HTTP-метод (мы отправляем GET-запрос), а post — это ресурс (мы запрашиваем конкретный пост, /posts/1)

    # 1. Отправляем GET-запрос на фейковый API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # 2. Проверяем, что сервер ответил (статус код 200)
    assert response.status_code == 200
    
    # 3. Проверяем, что в ответе есть нужное поле
    data = response.json() # Это метод, который преобразует тело ответа (которое приходит в формате JSON) в словарь Python. data становится словарём, к которому можно обращаться по ключам: data["id"], data["title"] и т.д.
    assert data["id"] == 1
    
'''
Что теперь делать (план на ближайшее время)
Напиши ещё один тест. Например, POST-запрос на создание поста:

Используй requests.post(url, json={"title": "foo", "body": "bar", "userId": 1})

Проверь статус-код и наличие id в ответе.

Вынеси URL в конфиг. Создай config/config.json:

json
{
    "base_url": "https://jsonplaceholder.typicode.com"
}
И читай его в тесте через json.load(). Это сделает код гибче.

Залей код на GitHub и добавь простой README.md с описанием проекта (это будет твоё портфолио).

GitHub Actions — настрой автоматический запуск тестов при каждом push. Это покажет, что ты умеешь работать с CI/CD.
'''
