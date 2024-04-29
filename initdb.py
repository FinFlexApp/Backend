from db.Tests.chapter import Chapter
from db import db_session
import random
import string
from datetime import datetime
from db.user import User
from db.Tests.chapterTest import ChapterTest
from db.Score.userTestAttempt import UserTestAttempt
from db.Score.testScores import TestScore

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
            'description': f'Test description for Chapter {i}, Test {j}'
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
# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
