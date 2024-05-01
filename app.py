import jwt, os
from flask import Flask, request, jsonify
from auth_middleware import token_required
from validate import *
from db.user import User
from db.Tests.chapter import Chapter
from db.Requires.userTestAccess import UserTestAccess
from db.Requires.userChapterAccess import UserChapterAccess
from db.Score.userTestAttempt import UserTestAttempt
from db import db_session
import datetime
from flask_cors import CORS
import json
from db.news import News
from db.Chat.chatBotHistory import ChatBotHistory
from db.Tests.chapterTest import ChapterTest
from db.Requires.ChapterRequires import ChapterRequire
from db.Requires.TestRequires import TestRequire
from db.Tests.testQuestion import TestQuestion
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models.gigachat import GigaChat
from db.Score.leaderBoard import LeaderBoard

chat = GigaChat(
    credentials='',
    verify_ssl_certs=False)
db_session.global_init("db/users.db")

# ________login&User&token________
app = Flask(__name__)
cors = CORS(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/users/register", methods=["POST"])
def add_user():
    session = db_session.create_session()
    try:
        datauser = json.loads(request.data)
        if not datauser:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        is_validated = validate_user(**datauser)
        if is_validated is not True:
            return dict(message='Invalid data', data=None, error=is_validated), 400
        if session.query(User).filter(User.email == datauser["email"]).first():
            return {
                "message": "User already exists",
                "error": "Conflict",
                "data": None
            }, 409
        user = User(
            email=datauser['email'],
            nickname=datauser['nickname'],
            firstname=datauser['firstname'],
            surname=datauser['surname'],
            img_src="https://upload.wikimedia.org/wikipedia/ru/5/51/%D0%9C%D0%B8%D0%BD%D1%8C%D0%BE%D0%BD%D1%8B_%28%D0%BF%D0%BE%D1%81%D1%82%D0%B5%D1%80%29.jpg",
            reg_date=datetime.datetime.now()
        )
        user.set_password(datauser["password"])
        session.add(user)
        session.commit()
        userChapterAccesses = UserChapterAccess(
            user_id=user.id,
            chapter_id=1,
            date=datetime.datetime.now()
        )
        session.add(userChapterAccesses)
        session.commit()
        userTestAccesses = UserTestAccess(
            user_id=user.id,
            test_id=1,
            date=datetime.datetime.now()
        )
        session.add(userTestAccesses)
        session.commit()
        return {
            "message": "Successfully created new user",
            "data": datauser
        }, 201
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


@app.route("/users/login", methods=["POST"])
def login():
    try:
        datauser = json.loads(request.data)
        if not datauser:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        is_validated = validate_email_and_password(datauser['email'], datauser['password'])
        if is_validated is not True:
            return dict(message='Invalid data', data=None, error=is_validated), 400
        session = db_session.create_session()
        user = session.query(User).filter(User.email == datauser["email"]).first()
        session.commit()
        if user.check_password(datauser['password']):
            try:
                datauser["token"] = jwt.encode(
                    {"user_id": user.id},
                    app.config["SECRET_KEY"],
                    algorithm="HS256"
                )
                datauser["user_id"] = user.id
                return {
                    "message": "Successfully fetched auth token",
                    "data": datauser
                }
            except Exception as e:
                return {
                    "error": "Something went wrong",
                    "message": str(e)
                }, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }, 404
    except Exception as e:
        return {
            "message": "Something went wrong!",
            "error": str(e),
            "data": None
        }, 500


@app.route("/users/getProfileData", methods=["POST"])
@token_required
def getProfileData():
    session = db_session.create_session()
    user_id = json.loads(request.data)['user_id']
    user = session.query(User).filter(User.id == user_id).first()
    d = {}
    for i in user.userTestAttempts:
        if i.test_id not in d:
            d[i.test_id] = 0
        d[i.test_id] = max(i.right_percent * i.test.testScore[0].max_score, d[i.test_id])
    answer = 0
    for j in d.keys():
        answer += d[j]
    return {"userId": user.id, "nickname": user.nickname, "surname": user.surname, "name": user.firstname,
            "img_src": user.img_src, "score": answer}


@app.route("/users/changePassword", methods=["POST"])
@token_required
def changePassword():
    session = db_session.create_session()
    user_id = json.loads(request.data)['user_id']
    oldPassword = json.loads(request.data)['oldPassword']
    newPassword = json.loads(request.data)['newPassword']
    user = session.query(User).filter(User.id == user_id).first()
    if user.check_password(oldPassword):
        user.set_password(newPassword)
        session.commit()
        return {"check": True}
    else:
        return {"check": False}


@app.route("/users/loadPicture", methods=["POST"])
@token_required
def loadPicture():
    session = db_session.create_session()
    user_id = json.loads(request.data)['user_id']
    url = json.loads(request.data)['url']
    user = session.query(User).filter(User.id == user_id).first()
    user.img_src = url
    session.commit()
    session.close()
    return {"check": True}


@app.route("/token", methods=["POST"])
def token():
    session = db_session.create_session()
    token = None
    if "Authorization" in request.headers:
        token = request.headers["Authorization"]
    if not token:
        return {"check": False}
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = session.query(User).get(data['user_id'])
        session.commit()
        if current_user is None:
            return {"check": False}
        return {"check": True}
    except Exception as e:
        return {"check": False}


# ________Test________
@app.route("/test/getchapters", methods=["POST"])
@token_required
def getchapters():
    user_id = json.loads(request.data)['user_id']
    session = db_session.create_session()
    chapters = session.query(Chapter).filter().all()
    answer = []
    for i in chapters:
        answer.append({"chapter_id": i.id, 'title': i.name})
        answer[-1]['is_unlocked'] = True if session.query(UserChapterAccess).filter(
            UserChapterAccess.user_id == user_id,
            UserChapterAccess.chapter_id == i.id).first() else False
        passed_tests = 0
        tests_count = 0
        chapter_score = 0
        for j in i.chapterTests:
            tests_count += 1
            a = session.query(UserTestAttempt).filter(UserTestAttempt.user_id == user_id,
                                                      UserTestAttempt.test_id == j.id).all()
            if a:
                passed_tests += 1
            max_score = 0
            for k in a:
                max_score = max(max_score, j.testScore[0].max_score * k.right_percent)
            chapter_score += max_score
        answer[-1]['sequence'] = i.sequence
        answer[-1]['passed_tests'] = passed_tests
        answer[-1]['tests_count'] = tests_count
        answer[-1]['chapter_score'] = chapter_score
        answer[-1]['description'] = i.description
        answer[-1]['img_src'] = i.source_url
    session.close()
    return answer


@app.route("/test/getChapterTests", methods=["POST"])
@token_required
def GetChapterTests():
    user_id = json.loads(request.data)['user_id']
    chapter_id = json.loads(request.data)['chapter_id']
    session = db_session.create_session()
    answer = []
    for i in session.query(Chapter).filter(Chapter.id == chapter_id).first().chapterTests:
        answer.append({})
        answer[-1]["test_id"] = i.id
        answer[-1]["title"] = i.name

        answer[-1]["is_unlocked"] = True if session.query(UserTestAccess).filter(UserTestAccess.user_id == user_id,
                                                                                 UserTestAccess.test_id == i.id).first() else False
        answer[-1]["questions_count"] = len(i.testQuestions)
        a = session.query(UserTestAttempt).filter(UserTestAttempt.user_id == user_id,
                                                  UserTestAttempt.test_id == i.id).all()
        answer[-1]["is_passed"] = True if a else False
        max_score = 0
        for k in a:
            max_score = max(max_score, i.testScore[0].max_score * k.right_percent)
        answer[-1]["user_score"] = max_score
        answer[-1]["max_score"] = i.testScore[0].max_score
        answer[-1]["img_src"] = i.img_src

    session.close()
    return answer


@app.route("/test/getQuestionsList", methods=["POST"])
@token_required
def getQuestionsList():
    session = db_session.create_session()
    test_id = json.loads(request.data)['test_id']
    answer = []
    for i in session.query(ChapterTest).filter(ChapterTest.id == test_id).first().testQuestions:
        answer.append({})
        answer[-1]["question_id"] = i.id
        answer[-1]["question_seq"] = i.sequence
        answer[-1]["question_text"] = i.text
    return answer


@app.route("/test/getQuestion", methods=["POST"])
@token_required
def getQuestion():
    session = db_session.create_session()
    question_id = json.loads(request.data)['question_id']
    question = session.query(TestQuestion).filter(TestQuestion.id == question_id).first()
    answer = {}
    answer['id'] = question.id
    answer['question_seq'] = question.sequence
    answer['question_text'] = question.text
    answer['question_attachment'] = question.img_src
    answer['multiple_choice'] = question.multiple_choice
    answer['answers'] = []
    for i in question.questionAnswers:
        answer['answers'].append(
            {"answers_id": i.id, "answer_text": i.text, "answer_attachment": i.img_src, "isRight": i.isRight})

    return answer


@app.route("/test/getFirstQuestion", methods=["POST"])
@token_required
def getFirstQuestion():
    session = db_session.create_session()
    test_id = json.loads(request.data)['test_id']
    quesions = []
    for i in session.query(ChapterTest).filter(ChapterTest.id == test_id).first().testQuestions:
        quesions.append(i)
    quesions = sorted(quesions, key=lambda x: x.sequence)
    question = quesions[0]
    answer = {}
    answer['id'] = question.id
    answer['question_seq'] = question.sequence
    answer['question_text'] = question.text
    answer['question_attachment'] = question.img_src
    answer['multiple_choice'] = question.multiple_choice
    answer['answers'] = []
    for i in question.questionAnswers:
        answer['answers'].append(
            {"answers_id": i.id, "answer_text": i.text, "answer_attachment": i.img_src, "isRight": i.isRight})

    return answer


@app.route("/test/getNextQuestion", methods=["POST"])
@token_required
def getNextQuestion():
    session = db_session.create_session()
    question_id = json.loads(request.data)['question_id']
    question = session.query(TestQuestion).filter(TestQuestion.id == question_id).first()
    questions = []
    for i in question.chapterTest.testQuestions:
        questions.append(i)
    questions = sorted(questions, key=lambda x: x.sequence)
    if len(questions) == question.sequence:
        return None
    else:
        question = questions[question.sequence]
        answer = {}
        answer['id'] = question.id
        answer['question_seq'] = question.sequence
        answer['question_text'] = question.text
        answer['question_attachment'] = question.img_src
        answer['multiple_choice'] = question.multiple_choice
        answer['answers'] = []
        for i in question.questionAnswers:
            answer['answers'].append(
                {"answers_id": i.id, "answer_text": i.text, "answer_attachment": i.img_src, "isRight": i.isRight})
        return answer


@app.route("/test/sendAnswers", methods=["POST"])
@token_required
def sendAnswers():
    answer = {}
    session = db_session.create_session()
    user_id = json.loads(request.data)['user_id']
    test_id = json.loads(request.data)['test_id']
    answers = json.loads(request.data)['submitted_answers']
    all_count = 0
    right_count = 0
    for i in answers:
        all_count += 1
        question = session.query(TestQuestion).filter(TestQuestion.id == i["question_id"]).first()
        if question.multiple_choice:
            if sorted(i["chosen_answers_ids"]) == sorted(
                    list(map(lambda x: x.id, filter(lambda x: x.isRight == True, question.questionAnswers)))):
                right_count += 1
        else:
            if i["chosen_answers_ids"][0] == list(filter(lambda x: x.isRight == True, question.questionAnswers))[0].id:
                right_count += 1
    tl = UserTestAttempt(
        user_id=user_id,
        test_id=test_id,
        date=datetime.datetime.now(),
        right_percent=right_count / all_count
    )
    session.add(tl)
    session.commit()
    a = session.query(ChapterTest).filter(ChapterTest.id == test_id).first()
    count_tests = 0
    for i in a.chapter.chapterTests:
        if session.query(UserTestAttempt).filter(UserTestAttempt.test_id == i.id, UserTestAttempt.user_id == user_id).first():
            count_tests += 1
    if count_tests == len(a.chapter.chapterTests):
        for i in session.query(ChapterRequire).filter(ChapterRequire.required_chapter_id == a.chapter.id).all():
            if not session.query(UserChapterAccess).filter(UserChapterAccess.user_id == user_id,
                                                           UserChapterAccess.chapter_id == i.unlockable_chapter_id).first():
                tl = UserChapterAccess(
                    user_id=user_id,
                    chapter_id=i.unlockable_chapter_id,
                    date=datetime.datetime.now(),
                )
                session.add(tl)
                tl = UserTestAccess(
                    user_id=user_id,
                    test_id=sorted(i.unlockable_chapter.chapterTests, key=lambda x: x.sequence)[0].id,
                    date=datetime.datetime.now(),
                )
                session.add(tl)
                session.commit()
    for i in session.query(TestRequire).filter(TestRequire.required_test_id == test_id).all():
        if not session.query(UserTestAccess).filter(UserTestAccess.user_id == user_id,
                                                    UserTestAccess.test_id == i.unlockable_test_id).first():
            tl = UserTestAccess(
                user_id=user_id,
                test_id=i.unlockable_test_id,
                date=datetime.datetime.now(),
            )
            session.add(tl)
            session.commit()
    answer["test_id"] = test_id
    answer["right_percent"] = right_count / all_count
    answer["points"] = right_count / all_count * session.query(ChapterTest).filter(ChapterTest.id == test_id).first().testScore[
        0].max_score
    session.close()
    return answer


# __News__
@app.route("/news", methods=["GET"])
@token_required
def news():
    session = db_session.create_session()
    answer = []
    for i in session.query(News).all():
        answer.append({})
        answer[-1]['title'] = i.title
        answer[-1]['preview_src'] = i.preview_src
        answer[-1]['text'] = i.text
        answer[-1]['date'] = i.date.strftime("%Y-%m-%d %H:%M:%S")
    session.close()
    return answer


# ______BOT______

@app.route("/Bot/sendMessage", methods=["POST"])
@token_required
def sendMessage():
    messages = [
        SystemMessage(
            content="Ты финансовый эксперт для детей, которые начинают изучать финасовую граммотность, будь вежлив"
        )
    ]
    user_id = json.loads(request.data)['user_id']
    text = json.loads(request.data)['text']
    session = db_session.create_session()
    old_messages = session.query(User).filter(User.id == user_id).first().chatBotHistories
    for i in old_messages:
        if i.isReplay:
            messages.append(AIMessage(
                content=i.text
            ))
        else:
            messages.append(HumanMessage(
                content=i.text
            ))
    messages.append(HumanMessage(
        content="User : " + text
    ))
    res = chat(messages)
    reply = res.content
    ch = ChatBotHistory(user_id=user_id, text=text, date=datetime.datetime.now(), isReplay=False)
    session.add(ch)
    ch = ChatBotHistory(user_id=user_id, text=reply, date=datetime.datetime.now(), isReplay=True)
    session.add(ch)
    session.commit()
    answer = {"message": reply, "date": ch.date.date.strftime("%Y-%m-%d %H:%M:%S")}

    return answer


@app.route("/bot/getChatHistory", methods=["POST"])
@token_required
def getChatHistory():
    session = db_session.create_session()
    user_id = json.loads(request.data)['user_id']
    answer = []
    for i in session.query(User).filter(User.id == user_id).first().chatBotHistories:
        answer.append({})
        answer[-1]['message'] = i.text
        answer[-1]['date'] = i.date.strftime("%Y-%m-%d %H:%M:%S")
        answer[-1]['isReply'] = i.isReplay
    session.close()
    return answer


# ______LB______
@app.route("/getLeaderBoard", methods=["POST"])
@token_required
def getLeaderBoard():
    session = db_session.create_session()
    N = json.loads(request.data)['N']
    answer = []
    a = sorted(session.query(LeaderBoard).all(), key=lambda x: -x.score)
    for i in a[:min(N, len(a))]:
        user = session.query()
        answer.append({"user_id": i.user.id, "nickname": i.user.nickname, "firstname": i.user.firstname, "surname": i.user.surname,
                       "img_src": i.user.img_src, "score": i.score, "tests_passed": i.tests_passed})
    session.close()
    return answer


# ______System________
@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        "message": "Forbidden",
        "error": str(e),
        "data": None
    }), 403


@app.errorhandler(404)
def forbidden(e):
    return jsonify({
        "message": "Endpoint Not Found",
        "error": str(e),
        "data": None
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
