import requests
import pytest

file = open("log.txt", "w")

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "6414ec5fd9ba158444b935c48388d5ae"
HEADER = {"Content-Type":"application/json", "trainer_token":TOKEN}
TRAINER_ID = "32482"

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_string_my_trainers():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == "32482"
    