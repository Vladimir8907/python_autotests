import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '14a7ae650ca0ec04e7fbbf7c4141cb0b'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_registration = { 
    "trainer_token": TOKEN,
    "email": "saraevvladimir59@gmail.com",
    "password": "qW140789"
}

body_confirmation = {"trainer_token": TOKEN
}

''''body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}'''

'''body_update = {
    "pokemon_id": "46680",
    "name": "New Names",
    "photo_id": 2
}'''

body_pokeball = {
    "pokemon_id": "46680"
}

'''response = requests.post(url = f'{URL}/trainers/reg',headers = HEADER, json = body_registration)

print(response.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_update = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_update)
print(response_update.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_pokeball)
print(response_pokeball.text)










