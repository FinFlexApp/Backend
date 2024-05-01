import requests
from json import dumps

# ________login&User&token________
# print(requests.get("http://127.0.0.1:5000/").text)
#
# print(requests.post("http://127.0.0.1:5000/users/register",
#                     data=dumps({"email": "12@1.ru", "nickname": "meow", "firstname": "meow", "surname": "meow",
#                                 "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}),
#                     headers={"Content-Type": "application/json"}).json())
#
# print(requests.post("http://127.0.0.1:5000/users/login",
#                     data=dumps({"email": "12@1.ru",
#                                 "password": "AbcabgGRGRbhdt4523tgrc12!!!!"}),
#                     headers={"Content-Type": "application/json"}).json())
#
# token = requests.post("http://127.0.0.1:5000/users/login",
#                       data=dumps({"email": "12@1.ru",
#                                   "password": "AbcabgGRGRbhdt4523tgrc123!!!!"}),
#                       headers={"Content-Type": "application/json"}).json()["data"]["token"]
#
# print(requests.post("http://127.0.0.1:5000/users/changePassword",
#                     data=dumps({"user_id": 11, "oldPassword": "AbcabgGRGRbhdt4523tgrc12!!!!",
#                                 "newPassword": "AbcabgGRGRbhdt4523tgrc123!!!!"}),
#                     headers={"Content-Type": "application/json",
#                              "Authorization": token}).json())
#
# token = requests.post("http://127.0.0.1:5000/users/login",
#                       data=dumps({"email": "12@1.ru",
#                                   "password": "AbcabgGRGRbhdt4523tgrc123!!!!"}),
#                       headers={"Content-Type": "application/json"}).json()["data"]["token"]
#
# print(requests.post("http://127.0.0.1:5000/users/getProfileData",
#                     data=dumps({"user_id": 11}),
#                     headers={"Content-Type": "application/json",
#                              "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/users/loadPicture",
#                     data=dumps({"user_id": 11, "url": "https://i.ytimg.com/vi/o47NEsDm2gw/maxresdefault.jpg"}),
#                     headers={"Content-Type": "application/json",
#                              "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/token", data=dumps({"user_id": 11}), headers={
#     "Authorization": token}).json())
#
# ____Test_____
# print(requests.post("http://127.0.0.1:5000/test/getchapters",
#                     data=dumps({"user_id": 11}), headers={"Content-Type": "application/json",
#                                                           "Authorization": token}).json())
# print(requests.post("http://127.0.0.1:5000/test/getChapterTests",
#                     data=dumps({"user_id": 11, "chapter_id": 1}), headers={"Content-Type": "application/json",
#                                                                            "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/test/getQuestionsList", data=dumps({"test_id": 1}), headers={
#     "Authorization": token}).json())
# print(requests.post("http://127.0.0.1:5000/test/getQuestion", data=dumps({"question_id": 2}), headers={
#     "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/test/getFirstQuestion", data=dumps({'test_id': 1}), headers={
#     "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/test/getNextQuestion", data=dumps({"question_id": 1}), headers={
#     "Authorization": token}).json())

# print(requests.post("http://127.0.0.1:5000/test/sendAnswers"
#                     , data=dumps({"user_id": 11, "test_id": 1,
#                                   "submitted_answers": [{"question_id": 1, "chosen_answers_ids": [1, 3]},
#                                                         {"question_id": 2, "chosen_answers_ids": [4]},
#                                                         {"question_id": 3, "chosen_answers_ids": [6, 8]}]}),
#                     headers={"Authorization": token}).json())

# print(requests.post("http://127.0.0.1:5000/test/sendAnswers",
#                     data=dumps({"user_id": 11, "test_id": 2,
#                                 "submitted_answers": [{"question_id": 4, "chosen_answers_ids": [1]},
#                                                       {"question_id": 5, "chosen_answers_ids": [2]},
#                                                       {"question_id": 6, "chosen_answers_ids": [3]}]}), headers={
#         "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/test/sendAnswers",
#                     data=dumps({"user_id": 11, "test_id": 3,
#                                 "submitted_answers": [{"question_id": 7, "chosen_answers_ids": [17, 19]},
#                                                       {"question_id": 8, "chosen_answers_ids": [20]},
#                                                       {"question_id": 9, "chosen_answers_ids": [1]}]}), headers={
#         "Authorization": token}).json())
# _____NEWS_______
# print(requests.get("http://127.0.0.1:5000/news", headers={
#     "Authorization": token}).json())
# _____BOT_______
# print(requests.post("http://127.0.0.1:5000/Bot/SendMessage", data=dumps({"user_id": 11, "text": "Кто ты?"}), headers={
#     "Authorization": token}).json())
#
# print(requests.post("http://127.0.0.1:5000/Bot/getChatHistory", data=dumps({"user_id": 11}), headers={
#     "Authorization": token}).json())

# _____LB______
# print(requests.post("http://127.0.0.1:5000/getLeaderBoard", data=dumps({"N": 4}), headers={
#     "Authorization": token}).json())
