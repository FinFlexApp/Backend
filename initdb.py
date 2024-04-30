from db.Tests.chapter import Chapter
from db import db_session
import random
import string
from datetime import datetime
from db.user import User
from db.Tests.chapterTest import ChapterTest
from db.Score.userTestAttempt import UserTestAttempt
from db.Score.testScores import TestScore
from db.Requires.userChapterAccess import UserChapterAccess
from db.Requires.userTestAccess import UserTestAccess
from db.Tests.questionAnswer import QuestionAnswer
from db.Tests.testQuestion import TestQuestion
from db.news import News

db_session.global_init("db/users.db")
chapters_data = [
    {'sequence': 1, 'name': 'Chapter 1', 'description': 'Description for Chapter 1',
     'source_url': 'https://example.com/chapter1'},
    {'sequence': 2, 'name': 'Chapter 2', 'description': 'Description for Chapter 2',
     'source_url': 'https://example.com/chapter2'},
    {'sequence': 3, 'name': 'Chapter 3', 'description': 'Description for Chapter 3',
     'source_url': 'https://example.com/chapter3'},
    {'sequence': 4, 'name': 'Chapter 4', 'description': 'Description for Chapter 4',
     'source_url': 'https://example.com/chapter4'},
    {'sequence': 5, 'name': 'Chapter 5', 'description': 'Description for Chapter 5',
     'source_url': 'https://example.com/chapter5'}
]
session = db_session.create_session()


# Генерация тестовых данных
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_email():
    return generate_random_string(8) + '@example.com'


def generate_nickname():
    return generate_random_string(8)


def generate_name():
    return generate_random_string(6)


def generate_password():
    return generate_random_string(10)


def generate_img_src():
    return 'https://example.com/' + generate_random_string(10)


def generate_reg_date():
    return datetime.now()


# Добавление тестовых данных в таблицу
for _ in range(10):
    user = User(email=generate_email(),
                nickname=generate_nickname(),
                firstname=generate_name(),
                surname=generate_name(),
                hashed_password=generate_password(),
                img_src=generate_img_src(),
                reg_date=generate_reg_date())
    session.add(user)

# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
# Добавление тестовых данных в таблицу
for chapter_data in chapters_data:
    chapter = Chapter(**chapter_data)
    session.add(chapter)

for i in range(1, 6):  # Считаем, что есть 5 глав в таблице "chapters"
    for j in range(1, 4):  # Генерируем по 3 теста для каждой главы
        test_data = {
            'chapter_id': i,
            'sequence': j,
            'name': f'Test {i}.{j}',
            'description': f'Test description for Chapter {i}, Test {j}',
            'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'
        }
        test = ChapterTest(**test_data)
        session.add(test)
test_ids = session.query(ChapterTest.id).all()

for test_id in test_ids:
    max_score = random.randint(20, 100)  # Генерируем случайное максимальное значение баллов
    score = TestScore(test_id=test_id[0], max_score=max_score)
    session.add(score)
user_ids = session.query(User.id).all()
test_ids = session.query(ChapterTest.id).all()

for _ in range(20):  # Генерируем 20 попыток тестирования
    user_id = random.choice(user_ids)[0]
    test_id = random.choice(test_ids)[0]
    date = datetime.now()
    right_percent = random.random()

    attempt = UserTestAttempt(user_id=user_id, test_id=test_id, date=date, right_percent=right_percent)
    session.add(attempt)

# user_id пользователя
user_id = 11

# chapter_id глав, к которым пользователь имеет доступ
chapter_ids = [1, 2, 3]

# Создаем записи доступа пользователя к главам
for chapter_id in chapter_ids:
    user_chapter_access = UserChapterAccess(user_id=user_id, chapter_id=chapter_id, date=datetime.now())
    session.add(user_chapter_access)

user_id = 11

# test_id тестов, к которым пользователь имеет доступ
test_ids = [1, 2, 3, 4, 5]

# Создаем записи доступа пользователя к тестам
for test_id in test_ids:
    user_test_access = UserTestAccess(user_id=user_id, test_id=test_id, date=datetime.now())
    session.add(user_test_access)

# ID теста, для которого будут созданы вопросы
test_id = 1

# Создаем вопросы для теста
questions_data = [
    {"sequence": 1, "text": "Question 1", "multiple_choice": True, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
    {"sequence": 2, "text": "Question 2", "multiple_choice": False, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
    {"sequence": 3, "text": "Question 3", "multiple_choice": True, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
]

for question_data in questions_data:
    question = TestQuestion(test_id=test_id, **question_data)
    session.add(question)
    session.flush()  # Получаем ID только что добавленного вопроса

    # Создаем ответы для вопроса
    if question_data["multiple_choice"]:
        answers_data = [
            {"text": "Answer 1", "isRight": True, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
            {"text": "Answer 2", "isRight": False, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
            {"text": "Answer 3", "isRight": True, 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
        ]
        for answer_data in answers_data:
            answer = QuestionAnswer(question_id=question.id, **answer_data)
            session.add(answer)

news_data = [
    {"title": "Новость 1", "preview_src": "http://example.com/image1.jpg", "text": "Текст новости 1",
     "date": datetime.now()},
    {"title": "Новость 2", "preview_src": "http://example.com/image2.jpg", "text": "Текст новости 2",
     "date": datetime.now()},
    {"title": "Новость 3", "preview_src": "http://example.com/image3.jpg", "text": "Текст новости 3",
     "date": datetime.now()},
]

for news_item in news_data:
    news = News(**news_item)
    session.add(news)
# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
