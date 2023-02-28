import requests
import json

status='available'
res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

info = {
"id": 2222,
"category": {"id": 2,"name": "Cat"},
"name": "Qwertyy",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res = requests.post(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"Статус ответа от сервера на POST запрос добавление питомца: {res.status_code}")
print(res.text)
print(res.json())
print(type(res.json()))

info = {
"id": 2222,
"category": {"id": 3,"name": "Cat"},
"name": "Tomas",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}
res = requests.put(f"https://petstore.swagger.io/v2/pet",
                                  headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                                  data = json.dumps(info, ensure_ascii=False))
print(f"изменение имени: {res.status_code}")
print(res.text)
print(res.json())
print(type(res.json()))

info = {
"id": 2222,
"category": {"id": 3,"name": "Cat"},
"name": "Tomas",
"photoUrls": ["string"],
"tags": [{"id": 0,"name": "string"}],
"status": "available"
}

res_del = requests.delete(f'https://petstore.swagger.io/v2/pet', headers={'accept': 'application/json'})
print(f"удаление: {res.status_code}")
print(res.text)
print(res.json())
print(type(res.json()))
