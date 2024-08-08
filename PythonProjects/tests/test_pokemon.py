import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '14a7ae650ca0ec04e7fbbf7c4141cb0b'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}


def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_responce():
    response_get = requests.get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : '6847'})
    assert response_get.json()["data"][0]["trainer_name"] == 'Testing'
