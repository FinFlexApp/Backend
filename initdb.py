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
from db.Requires.ChapterRequires import ChapterRequire
from db.Requires.TestRequires import TestRequire

db_session.global_init("db/users.db")
chapters_data = [
    {'sequence': 1, 'name': 'Путешествие в Мир Денег', 'description': 'Добро пожаловать в увлекательное путешествие в Мир Денег! Здесь мы узнаем, как правильно обращаться с деньгами, чтобы они всегда были на твоей стороне. Готовы к приключению?',
     'source_url': 'https://kartinkis.cdnbro.com/posts/48828606-finansovaia-gramotnost-art-1.jpg'},
    {'sequence': 2, 'name': 'Сокровища Финансовой Мудрости', 'description': 'Добро пожаловать в Сокровища Финансовой Мудрости! Здесь мы раскроем секреты того, как делать правильные решения с деньгами и сделаем тебя настоящим экспертом в финансах.',
     'source_url': 'https://www.tartaria.ru/Tartaria/ContentAttachments/401913/5289d911-76cb-461b-a412-aaf3746f5e43.jpg'},
    {'sequence': 3, 'name': 'Волшебные Ключи Финансового Успеха', 'description': 'Добро пожаловать в мир Волшебных Ключей Финансового Успеха! Здесь мы научимся использовать магию денег, чтобы добиться всех своих желаний и мечтаний.',
     'source_url': 'http://klubmama.ru/uploads/posts/2022-09/1662180459_19-klubmama-ru-p-podelki-na-temu-finansovaya-gramotnost-fot-22.jpg'},
    {'sequence': 4, 'name': 'Приключения Денежного Мастера', 'description': 'Добро пожаловать в увлекательные Приключения Денежного Мастера! Здесь мы станем настоящими экспертами в управлении деньгами и научимся применять наши навыки в реальной жизни.',
     'source_url': 'https://thumbs.dreamstime.com/b/%D0%BA%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F-%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%80%D0%BE%D1%81%D1%82%D0%B0-%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BE%D0%BA%D1%83%D0%BF%D0%B0%D0%B5%D0%BC%D0%BE%D1%81%D1%82%D0%B8-161105553.jpg'},
    {'sequence': 5, 'name': 'Финансовые Приключения', 'description': 'Добро пожаловать в захватывающие Финансовые Приключения! В этой главе мы отправимся в увлекательное путешествие по миру денег и научимся преодолевать финансовые препятствия.',
     'source_url': 'https://img.freepik.com/premium-vector/money-bag-gold-coins-and-upward-arrow-graph-growth_349999-812.jpg?size=626&ext=jpg'}
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
    return 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'


def generate_reg_date():
    return datetime.now()


# Закрытие сессии
session.close()
# Добавление тестовых данных в таблицу
for chapter_data in chapters_data:
    chapter = Chapter(**chapter_data)
    session.add(chapter)
for i in range(2, 6):
    chapter_require1 = ChapterRequire(unlockable_chapter_id=i, required_chapter_id=i - 1)
    session.add(chapter_require1)
    session.commit()

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
        session.commit()
        if j != 1:
            chapter_require1 = TestRequire(unlockable_test_id=test.id, required_test_id=test.id - 1)
            session.add(chapter_require1)
            session.commit()
test_ids = session.query(ChapterTest.id).all()

for test_id in test_ids:
    max_score = random.randint(20, 100)  # Генерируем случайное максимальное значение баллов
    score = TestScore(test_id=test_id[0], max_score=max_score)
    session.add(score)

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
    session.commit()
    userChapterAccess = UserChapterAccess(
        user_id=user.id,
        chapter_id=1,
        date=datetime.now()
    )
    userTestAccess = UserTestAccess(
        user_id=user.id,
        test_id=1,
        date=datetime.now()
    )
    session.add(userChapterAccess)
    session.add(userTestAccess)
    session.commit()
# Сохранение изменений
session.commit()
user_ids = session.query(User.id).all()
test_ids = session.query(ChapterTest.id).all()

# for _ in range(20):  # Генерируем 20 попыток тестирования
#     user_id = random.choice(user_ids)[0]
#     test_id = random.choice(test_ids)[0]
#     date = datetime.now()
#     right_percent = random.random()
#
#     attempt = UserTestAttempt(user_id=user_id, test_id=test_id, date=date, right_percent=right_percent)
#     session.add(attempt)

# ID теста, для которого будут созданы вопросы
test_id = 1

# Создаем вопросы для теста
questions_data = [
    {"sequence": 1, "text": "Question 1", "multiple_choice": True,
     'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
    {"sequence": 2, "text": "Question 2", "multiple_choice": False,
     'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
    {"sequence": 3, "text": "Question 3", "multiple_choice": True,
     'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
]
for i in range(1, 16):
    for question_data in questions_data:
        question = TestQuestion(test_id=i, **question_data)
        session.add(question)
        session.flush()  # Получаем ID только что добавленного вопроса

        # Создаем ответы для вопроса
        if question_data["multiple_choice"]:
            answers_data = [
                {"text": "Answer 1", "isRight": True,
                 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
                {"text": "Answer 2", "isRight": False,
                 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
                {"text": "Answer 3", "isRight": True,
                 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
            ]
            for answer_data in answers_data:
                answer = QuestionAnswer(question_id=question.id, **answer_data)
                session.add(answer)
        else:
            answers_data = [
                {"text": "Answer 1", "isRight": True,
                 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'},
                {"text": "Answer 2", "isRight": False,
                 'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
            ]
            for answer_data in answers_data:
                answer = QuestionAnswer(question_id=question.id, **answer_data)
                session.add(answer)
news_data = [
    {"title": "Вместе с командой Python Google уволила команды Flutter и Dart", "preview_src": "https://habrastorage.org/r/w780/getpro/habr/upload_files/8aa/734/17f/8aa73417ffa436d79fd4ae72ddfef4f4.jpg", "text": """Google сократила сотрудников нескольких команд. Помимо команды разработки и поддержки Python, мест в компании лишились члены команд Flutter и Dart. Google подтвердила увольнения изданию TechCrunch, но не назвала конкретные должности и число уволенных.

Представитель Google заявил изданию, что компания «инвестирует в самые приоритетные направления» и «вносит изменения, чтобы стать эффективнее и лучше работать, сократить бюрократию и многоуровневость». В компании также добавили, что увольнения стали частью реорганизации, а затронутые сотрудники смогут подать заявку на другие открытые вакансии в Google.""",
     "date": datetime.now()},
    {"title": "В Политехе пройдет хакатон по веб-разработке «Цифровой ВУЗ»", "preview_src": "https://www.sstu.ru/upload/iblock/cc6/veb.png", "text": """13-15 мая в Саратовском государственном техническом университете имени Гагарина Ю.А. пройдет вебинар по веб-разработке «Цифровой ВУЗ».
Принять участие могут команды в составе до четырех человек.

Положение, список кейсов и регистрация – на сайте. Регистрация открыта до 7 мая.

Хакатон пройдет на базе Института прикладных информационных технологий и коммуникаций в рамках Международного конкурса компьютерных работ среди детей, юношества и студенческой молодежи «Цифровой ветер».""",
     "date": datetime.now()},
    {"title": "Импорт российской нефти в Индию достиг максимума за девять месяцев", "preview_src": "https://s0.rbk.ru/v6_top_pics/resized/590xH/media/img/5/99/347147178239995.webp", "text": """Индия на 19% нарастила импорт нефти из России в апреле, его объем составил 1,96 млн барр. в сутки, что стало рекордным показателем за последние девять месяцев, пишет The Indian Express""",
     "date": datetime.now()},
]

for news_item in news_data:
    news = News(**news_item)
    session.add(news)
# Сохранение изменений
session.commit()

# Закрытие сессии
session.close()
