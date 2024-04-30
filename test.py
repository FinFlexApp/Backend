import requests
from json import dumps
#
# # ____login_____
# print(requests.post("http://127.0.0.1:5000/users/register",
#                     data=dumps({"email": "12@1.ru", "nickname": "meow", "firstname": "meow", "surname": "meow",
#                                        "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}),
#                     headers={"Content-Type": "application/json"}).json())
#
# b = requests.post("http://127.0.0.1:5000/users/login",
#                   data=dumps({"email": "12@1.ru",
#                         "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}),
#                   headers={"Content-Type": "application/json"}).json()
# print(b)
#
# # ____Test_____
b = requests.post("http://127.0.0.1:5000/test/getchapters",
                  data=dumps({"user_id": 11}), headers={"Content-Type": "application/json",
                                                 "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMX0.00KV-iWi85eL-CZC4w5Ma2r0_dMw8ohjbjDkStIIXfQ"})
print(b.text)
b = requests.post("http://127.0.0.1:5000/test/getChapterTests",
                  data=dumps({"user_id": 11, "chapter_id": 2}), headers={"Content-Type": "application/json",
                                                                  "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMX0.00KV-iWi85eL-CZC4w5Ma2r0_dMw8ohjbjDkStIIXfQ"})

print(b.text)

#
# print(requests.get("http://127.0.0.1:5000/users/", headers={"Authorization": b['data']['token']}).text)
