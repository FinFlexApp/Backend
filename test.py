import requests

# print(requests.post("http://127.0.0.1:5000/users/register",
#                     json={"email": "12@1.ru", "nickname": "meow", "firstname": "meow", "surname": "meow",
#                           "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}).text)
#
# b = requests.post("http://127.0.0.1:5000/users/login",
#                   json={"email": "12@1.ru",
#                         "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}).json()
# print(b)
b = requests.get("http://127.0.0.1:5000/test/getchapters",
                  json={"user_id": 11}, headers={"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMX0.00KV-iWi85eL-CZC4w5Ma2r0_dMw8ohjbjDkStIIXfQ"})


print(b.json())










#
# print(requests.get("http://127.0.0.1:5000/users/", headers={"Authorization": b['data']['token']}).text)
