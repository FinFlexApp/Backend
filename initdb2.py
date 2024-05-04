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
    {'sequence': 1, 'name': 'Что такое деньги?',
     'description': 'В этой главе дети узнают, что такое деньги, как они используются в повседневной жизни и почему важно уметь с ними обращаться.',
     'source_url': 'https://kartinkis.cdnbro.com/posts/48828606-finansovaia-gramotnost-art-1.jpg'},
    {'sequence': 2, 'name': 'Разумное планирование расходов',
     'description': 'В этой главе дети изучат основные принципы бюджетирования, учатся планировать свои расходы на игрушки, развлечения и другие важные вещи.',
     'source_url': 'https://www.tartaria.ru/Tartaria/ContentAttachments/401913/5289d911-76cb-461b-a412-aaf3746f5e43.jpg'},
    {'sequence': 3, 'name': 'Значение сбережений',
     'description': 'В этой главе дети узнают о важности сбережений и как они могут помочь в достижении целей, будь то покупка игрушки или совершение путешествия.',
     'source_url': 'http://klubmama.ru/uploads/posts/2022-09/1662180459_19-klubmama-ru-p-podelki-na-temu-finansovaya-gramotnost-fot-22.jpg'},
    {'sequence': 4, 'name': 'Различие между нужными и лишними расходами',
     'description': 'Дети научатся различать между тем, что им действительно нужно, и тем, что является лишним тратами. Это поможет им принимать более осознанные финансовые решения.',
     'source_url': 'https://thumbs.dreamstime.com/b/%D0%BA%D0%BE%D0%BD%D1%86%D0%B5%D0%BF%D1%86%D0%B8%D1%8F-%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE-%D1%80%D0%BE%D1%81%D1%82%D0%B0-%D1%84%D0%B8%D0%BD%D0%B0%D0%BD%D1%81%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BE%D0%BA%D1%83%D0%BF%D0%B0%D0%B5%D0%BC%D0%BE%D1%81%D1%82%D0%B8-161105553.jpg'},
    {'sequence': 5, 'name': 'Заработок и ответственность',
     'description': 'В последней главе дети изучат концепцию заработка денег, понятие труда и ответственности за свои финансовые решения. Они также узнают о различных способах заработка денег, начиная с помощи родителей и заканчивая выполняемыми ими заданиями.',
     'source_url': 'https://img.freepik.com/premium-vector/money-bag-gold-coins-and-upward-arrow-graph-growth_349999-812.jpg?size=626&ext=jpg'}
]
session = db_session.create_session()

for chapter_data in chapters_data:
    chapter = Chapter(**chapter_data)
    session.add(chapter)
for i in range(2, 6):
    chapter_require1 = ChapterRequire(unlockable_chapter_id=i, required_chapter_id=i - 1)
    session.add(chapter_require1)
    session.commit()

test = [
    [
        {
            "name": "Определение денег",
            "description": "В этой части мы рассмотрим, что такое деньги и как они используются для обмена товарами и услугами в экономике.",
            "sequence": 1
        },
        {
            "name": "Использование денег",
            "description": "В этой части мы обсудим, как вы, дети, используете деньги для покупки товаров и услуг в повседневной жизни.",
            "sequence": 2
        },
        {
            "name": "Значение финансовой грамотности",
            "description": "Здесь вы, дети, поймете, почему важно уметь управлять деньгами и как это может повлиять на ваше будущее.",
            "sequence": 3
        }
    ],
    [
        {
            "name": "Основы бюджетирования",
            "description": "В этой части мы рассмотрим основные принципы составления бюджета и почему важно управлять своими финансами.",
            "sequence": 1
        },
        {
            "name": "Планирование расходов",
            "description": "Здесь вы, дети, научитесь планировать свои траты на различные цели, такие как игрушки, развлечения и другие важные вещи.",
            "sequence": 2
        },
        {
            "name": "Умение экономить",
            "description": "В этой части мы обсудим важность экономии и различные методы, которые помогут вам сохранять деньги для будущих целей.",
            "sequence": 3
        }
    ],
    [
        {
            "name": "Понимание сбережений",
            "description": "Здесь вы, дети, узнаете, почему сбережения важны для достижения ваших финансовых целей.",
            "sequence": 1
        },
        {
            "name": "Цели сбережений",
            "description": "В этой части рассмотрим, какие цели можно достичь благодаря сбережениям, будь то покупка игрушек, кружков или путешествий.",
            "sequence": 2
        },
        {
            "name": "Методы сбережений",
            "description": "Здесь вы, дети, узнаете о различных способах сбережения, таких как откладывание денег в копилку или открытие банковского счета.",
            "sequence": 3
        }
    ],
    [
        {
            "name": "Определение нужных расходов",
            "description": "Здесь вы, дети, учиться определять, что является действительно необходимыми тратами для вашей повседневной жизни.",
            "sequence": 1
        },
        {
            "name": "Определение лишних расходов",
            "description": "В этой части рассмотрим различные виды лишних трат и способы их избегания.",
            "sequence": 2
        },
        {
            "name": "Принятие осознанных финансовых решений",
            "description": "Здесь вы, дети, узнаете, как различать между нужными и лишними расходами, чтобы принимать более осознанные решения о своих финансах.",
            "sequence": 3
        }
    ],
    [
        {
            "name": "Концепция заработка денег",
            "description": "Здесь вы, дети, узнаете, что такое заработок денег и как он связан с понятием труда и ответственности.",
            "sequence": 1
        },
        {
            "name": "Различные способы заработка",
            "description": "В этой части рассмотрим различные способы заработка денег, начиная с помощи родителей и заканчивая выполнением различных заданий.",
            "sequence": 2
        },
        {
            "name": "Ответственность за финансовые решения",
            "description": "Здесь вы, дети, узнаете о важности принятия ответственности за свои финансовые решения и их последствия.",
            "sequence": 3
        }
    ]
]
question = [{
    "text": "Что представляют собой деньги?",
    "sequence": 0,
    "multiple_choice": 0,
},
    {
        "text": "Какая функция денег в экономике?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных функций выполняют деньги?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Что можно купить с помощью денег?",
        "sequence": 0,
        "multiple_choice": 0
    },
    {
        "text": "Какие из перечисленных вещей можно купить за деньги?",
        "sequence": 1,
        "multiple_choice": 0
    },
    {
        "text": "Какие из перечисленных покупок являются возможными с использованием денег?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Почему важно уметь управлять деньгами?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Как финансовая грамотность может повлиять на ваше будущее?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие навыки входят в концепцию финансовой грамотности?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Что такое бюджет?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Зачем составлять бюджет?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие основные шаги включает в себя составление бюджета?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Зачем важно планировать свои расходы?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какие виды трат следует планировать?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие инструменты помогают в планировании расходов?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Почему важно уметь экономить?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какие методы помогают сохранять деньги?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных действий способствуют экономии?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Почему важно иметь сбережения?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какие методы помогают накапливать сбережения?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных действий способствуют накоплению сбережений?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Какие из перечисленных могут быть целями сбережений?",
        "sequence": 0,
        "multiple_choice": 1,
    },
    {
        "text": "Что можно сделать, сэкономив некоторую сумму?",
        "sequence": 1,
        "multiple_choice": 0
    },
    {
        "text": "Почему важно устанавливать цели для сбережений?",
        "sequence": 2,
        "multiple_choice": 0,
    },
    {
        "text": "Какой из способов является методом сбережений?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Что можно сделать для того, чтобы начать сберегать деньги?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных являются методами сбережений?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Что является примером нужных расходов?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какой из нижеперечисленных расходов является необходимым?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных расходов считаются нужными для жизни?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Что является примером лишних расходов?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какой из нижеперечисленных расходов считается лишним?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие из перечисленных расходов можно считать лишними?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Что поможет вам принимать осознанные финансовые решения?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какие действия помогут вам различать между нужными и лишними расходами?",
        "sequence": 1,
        "multiple_choice": 0
    },
    {
        "text": "Какие из нижеперечисленных действий помогут вам принимать более осознанные финансовые решения?",
        "sequence": 2,
        "multiple_choice": 0,
    },
    {
        "text": "Что такое заработок денег?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Как связан заработок денег с понятием труда?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какая ответственность сопровождает заработок денег?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Какие способы заработка денег могут начинаться с помощи родителей?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какой способ заработка денег включает выполнение различных заданий?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие способы заработка денег доступны для детей?",
        "sequence": 2,
        "multiple_choice": 1,
    },
    {
        "text": "Почему важно принимать ответственность за свои финансовые решения?",
        "sequence": 0,
        "multiple_choice": 0,
    },
    {
        "text": "Какие последствия могут быть, если не принимать ответственность за финансовые решения?",
        "sequence": 1,
        "multiple_choice": 0,
    },
    {
        "text": "Какие действия можно считать проявлением ответственности за финансовые решения?",
        "sequence": 2,
        "multiple_choice": 0,
    }
]
answers = [[
    {"text": "Бумажные купюры", "isRight": False},
    {"text": "Средство обмена", "isRight": True}
], [
    {"text": "Украшение", "isRight": False},
    {"text": "Средство обмена", "isRight": True}
], [
    {"text": "Средство обмена", "isRight": True},
    {"text": "Средство коммуникации", "isRight": True},
    {"text": "Средство транспортировки", "isRight": False}
], [
    {"text": "Воздух", "isRight": False},
    {"text": "Товары и услуги", "isRight": True}
],
    [
        {"text": "Счастье", "isRight": False},
        {"text": "Еда и одежда", "isRight": True}
    ],
    [
        {"text": "Космический корабль", "isRight": False},
        {"text": "Книга", "isRight": True},
        {"text": "Невидимка", "isRight": False}
    ],
    [
        {"text": "Потому что можно купить много игрушек", "isRight": False},
        {"text": "Потому что это помогает достигать финансовых целей", "isRight": True}
    ],
    [
        {"text": "Не повлияет", "isRight": False},
        {"text": "Поможет принимать осознанные финансовые решения", "isRight": True}
    ],
    [
        {"text": "Тратить все деньги на развлечения", "isRight": False},
        {"text": "Умение планировать бюджет", "isRight": True},
        {"text": "Не заботиться о деньгах", "isRight": False}
    ],
    [
        {"text": "Способ получения дополнительного дохода", "isRight": False},
        {"text": "План распределения денег на различные нужды", "isRight": True}
    ],
    [
        {"text": "Для того, чтобы тратить деньги на что угодно", "isRight": False},
        {"text": "Для контроля над финансами и достижения финансовых целей", "isRight": True}
    ],
    [
        {"text": "Не имеет значения, как составлять бюджет", "isRight": False},
        {"text": "Определение доходов и расходов, установление приоритетов в трате", "isRight": True},
        {"text": "Тратить деньги без планирования", "isRight": False}
    ],
    [
        {"text": "Чтобы тратить деньги на все, что хочется", "isRight": False},
        {"text": "Для эффективного использования денег и достижения поставленных целей", "isRight": True}
    ],
    [
        {"text": "Только на игрушки", "isRight": False},
        {"text": "На развлечения и другие важные вещи", "isRight": True}
    ],
    [
        {"text": "Никакие, можно тратить деньги без планирования", "isRight": False},
        {"text": "Бюджеты, списки покупок, приоритеты", "isRight": True},
        {"text": "Инвестирование", "isRight": False}
    ],
    [
        {"text": "Для того чтобы тратить деньги без оглядки", "isRight": False},
        {"text": "Для достижения финансовых целей и обеспечения финансовой стабильности", "isRight": True}
    ],
    [
        {"text": "Только инвестирование", "isRight": False},
        {"text": "Экономия на покупках, откладывание части доходов, разумное планирование расходов",
         "isRight": True}
    ],
    [
        {"text": "Откладывание денег на счет в банке", "isRight": True},
        {"text": "Покупка вещей без проверки их цен", "isRight": False},
        {"text": "Регулярное пополнение копилки", "isRight": True}
    ],
    [
        {"text": "Для того чтобы тратить деньги без оглядки", "isRight": False},
        {"text": "Для достижения финансовых целей и обеспечения финансовой стабильности", "isRight": True}
    ],
    [
        {"text": "Только тратить меньше, чем зарабатываешь", "isRight": False},
        {"text": "Откладывание части доходов, экономия на покупках", "isRight": True}
    ],
    [
        {"text": "Откладывание денег на счет в банке", "isRight": True},
        {"text": "Покупка вещей без проверки их цен", "isRight": False},
        {"text": "Регулярное пополнение копилки", "isRight": True}
    ],
    [
        {"text": "Покупка дорогой машины", "isRight": True},
        {"text": "Ежедневные траты на еду", "isRight": False},
        {"text": "Оплата обучения в университете", "isRight": True}
    ],
    [
        {"text": "Купить новую игрушку", "isRight": False},
        {"text": "Оплатить курс дополнительного образования", "isRight": True}
    ],
    [
        {"text": "Для того чтобы потом потратить все накопленные деньги", "isRight": False},
        {"text": "Для осуществления своих мечт", "isRight": True}
    ],
    [
        {"text": "Покупка новой игрушки", "isRight": False},
        {"text": "Откладывание денег в копилку", "isRight": True}
    ],
    [
        {"text": "Не покупать ничего нового", "isRight": False},
        {"text": "Установить конкретную цель для сбережений", "isRight": True}
    ],
    [
        {"text": "Открытие банковского счета", "isRight": True},
        {"text": "Расходование всех денег сразу", "isRight": False},
        {"text": "Покупка новых игрушек каждый день", "isRight": False}
    ],
    [
        {"text": "Покупка ежедневного обеда в столовой", "isRight": True},
        {"text": "Покупка новой игрушки каждый день", "isRight": False}
    ],
    [
        {"text": "Покупка продуктов питания", "isRight": True},
        {"text": "Покупка дополнительного набора карандашей для рисования", "isRight": False}
    ],
    [
        {"text": "Оплата коммунальных услуг", "isRight": True},
        {"text": "Покупка новых игр для игровой консоли", "isRight": False},
        {"text": "Покупка новой пары кроссовок каждую неделю", "isRight": False}
    ],
    [
        {"text": "Покупка ежедневной порции мороженого", "isRight": False},
        {"text": "Покупка новой пары кроссовок, когда старая еще в хорошем состоянии", "isRight": True}
    ],
    [
        {"text": "Оплата абонемента в спортивный клуб", "isRight": False},
        {"text": "Покупка нового компьютера для учебы", "isRight": True}
    ],
    [
        {"text": "Покупка новой одежды каждую неделю", "isRight": True},
        {"text": "Покупка книг для самообразования", "isRight": False},
        {"text": "Оплата регулярных занятий в музыкальной школе", "isRight": False}
    ],
    [
        {"text": "Покупка всего, что захочется без размышлений", "isRight": False},
        {"text": "Оценка нужности и целесообразности расходов", "isRight": True}
    ],
    [
        {"text": "Проведение анализа своих финансов и составление бюджета", "isRight": True},
        {"text": "Покупка всего, что понравится без оглядки на цену", "isRight": False}
    ],
    [
        {"text": "Составление списка желаемых покупок и их моментальное приобретение", "isRight": False},
        {"text": "Планирование расходов и установление приоритетов", "isRight": True}
    ],
    [
        {"text": "Процесс получения денежного вознаграждения за выполненную работу", "isRight": True},
        {"text": "Получение денег от родственников без каких-либо усилий", "isRight": False}
    ],
    [
        {"text": "Заработок денег всегда происходит без труда", "isRight": False},
        {"text": "Чем больше работаешь, тем больше зарабатываешь", "isRight": True}
    ],
    [
        {"text": "Ответственность перед родственниками за полученные деньги", "isRight": False},
        {"text": "Ответственность за правильное использование и управление заработанными средствами",
         "isRight": True}
    ],
    [
        {"text": "Получение денежного вознаграждения за выполненные домашние дела", "isRight": True},
        {"text": "Получение денег в подарок от родителей без каких-либо условий", "isRight": False}
    ],
    [
        {"text": "Работа в крупной компании", "isRight": True},
        {"text": "Получение карманных денег от родственников", "isRight": False}
    ],
    [
        {"text": "Помощь родителям в домашних делах", "isRight": True},
        {"text": "Участие во внеклассных мероприятиях", "isRight": True}
    ],
    [
        {"text": "Чтобы не тратить слишком много денег", "isRight": False},
        {"text": "Чтобы избежать финансовых проблем в будущем", "isRight": True}
    ],
    [
        {"text": "Рост благосостояния и увеличение сбережений", "isRight": False},
        {"text": "Финансовые проблемы и долги", "isRight": True}
    ],
    [
        {"text": "Планирование бюджета и ограничение лишних трат", "isRight": True},
        {"text": "Бездумное расходование денег на всякие мелочи", "isRight": False}
    ]
]

for c in range(5):  # Считаем, что есть 5 глав в таблице "chapters"
    for t in range(3):  # Генерируем по 3 теста для каждой главы
        test_data = {
            'chapter_id': c + 1,
            'sequence': test[c][t]['sequence'],
            'name': test[c][t]['name'],
            'description': test[c][t]['description'],
            'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'
        }
        test1 = ChapterTest(**test_data)
        session.add(test1)
        session.commit()
        if t != 0:
            chapter_require1 = TestRequire(unlockable_test_id=test1.id, required_test_id=test1.id - 1)
            session.add(chapter_require1)
            session.commit()
        for q in range(3):
            question_data = {"sequence": question[c * 5 + t * 3 + q]['sequence'],
                             "text": question[c * 5 + t * 3 + q]['text'],
                             "multiple_choice": question[c * 5 + t * 3 + q]['multiple_choice'],
                             'img_src': 'https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg'}
            question1 = TestQuestion(test_id=test1.id, **question_data)
            session.add(question1)
            session.flush()
            for a in answers[question1.id - 1]:
                answer = QuestionAnswer(question_id=question1.id,
                                        img_src='https://thumbs.dfs.ivi.ru/storage6/contents/2/f/3d8cf3a06154802d89099ff0812641.jpg',
                                        **a)
                session.add(answer)
test_ids = session.query(ChapterTest.id).all()

for test_id in test_ids:
    max_score = random.randint(80, 140)  # Генерируем случайное максимальное значение баллов
    score = TestScore(test_id=test_id[0], max_score=max_score)
    session.add(score)
news_data = [
    {"title": "Вместе с командой Python Google уволила команды Flutter и Dart",
     "preview_src": "https://habrastorage.org/r/w780/getpro/habr/upload_files/8aa/734/17f/8aa73417ffa436d79fd4ae72ddfef4f4.jpg",
     "text": """Google сократила сотрудников нескольких команд. Помимо команды разработки и поддержки Python, мест в компании лишились члены команд Flutter и Dart. Google подтвердила увольнения изданию TechCrunch, но не назвала конкретные должности и число уволенных.

Представитель Google заявил изданию, что компания «инвестирует в самые приоритетные направления» и «вносит изменения, чтобы стать эффективнее и лучше работать,
 сократить бюрократию и многоуровневость». В компании также добавили, что увольнения стали частью реорганизации, а затронутые сотрудники смогут подать заявку на
  другие открытые вакансии в Google.""",
     "date": datetime.now()},
    {"title": "В Политехе пройдет хакатон по веб-разработке «Цифровой ВУЗ»",
     "preview_src": "https://www.sstu.ru/upload/iblock/cc6/veb.png", "text": """13-15 мая в Саратовском государственном техническом университете имени Гагарина Ю.А. пройдет вебинар по веб-разработке «Цифровой ВУЗ».
Принять участие могут команды в составе до четырех человек.

Положение, список кейсов и регистрация – на сайте. Регистрация открыта до 7 мая.

Хакатон пройдет на базе Института прикладных информационных технологий и коммуникаций в рамках Международного конкурса компьютерных работ среди детей, юношества и студенческой молодежи «Цифровой ветер».""",
     "date": datetime.now()},
    {"title": "Импорт российской нефти в Индию достиг максимума за девять месяцев",
     "preview_src": "https://s0.rbk.ru/v6_top_pics/resized/590xH/media/img/5/99/347147178239995.webp",
     "text": """Индия на 19% нарастила импорт нефти из России в апреле, его объем составил 1,96 млн барр. в сутки, что стало рекордным показателем за последние девять месяцев, пишет The Indian Express""",
     "date": datetime.now()},
]

for news_item in news_data:
    news = News(**news_item)
    session.add(news)
session.commit()
session.close()
