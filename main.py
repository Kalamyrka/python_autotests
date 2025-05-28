import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6414ec5fd9ba158444b935c48388d5ae"
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN}

body_create = {
    "name": "Циклопентанпергидрофенантрен",
    "photo_id": 524
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) # Запрос на создание покемона
print(response_create.text)

pokemon_id = response_create.json()['id'] # Запись ID покемона в новую переменную

response_rename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = {"pokemon_id": pokemon_id, "name": "Тринитротолуол"}) # Запрос на изменение имени покемона
print(response_rename.text)

response_capture = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = {"pokemon_id": pokemon_id}) # Запрос на поимку покемона
print(response_capture.text)
