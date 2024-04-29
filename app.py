import jwt, os
from flask import Flask, request, jsonify
from auth_middleware import token_required
from validate import *
from db.user import User
from db.Tests.chapter import Chapter
from db.Score.userTestAttempt import UserTestAttempt
from db import db_session
import datetime
from flask_cors import CORS, cross_origin

db_session.global_init("db/users.db")

# ________login________
app = Flask(__name__)
cors = CORS(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello():
    return "Hello World!"


@app.route("/users/register", methods=["POST"])
@cross_origin()
def add_user():
    session = db_session.create_session()
    try:
        datauser = request.json
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
@cross_origin()
def login():
    try:
        datauser = request.json
        if not datauser:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request"
            }, 400
        # validate input
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


@app.route("/users/", methods=["GET"])
@token_required
@cross_origin()
def get_current_user(current_user):
    return jsonify({
        "message": "successfully retrieved user profile",
        "data": current_user
    })


@app.errorhandler(403)
@cross_origin()
def forbidden(e):
    return jsonify({
        "message": "Forbidden",
        "error": str(e),
        "data": None
    }), 403


@app.errorhandler(404)
@cross_origin()
def forbidden(e):
    return jsonify({
        "message": "Endpoint Not Found",
        "error": str(e),
        "data": None
    }), 404


# ________Test________
@app.route("/test/getchapters", methods=["POST"])
@token_required
@cross_origin()
def getchapters():
    user_id = request.json['user_id']
    session = db_session.create_session()
    chapters = session.query(Chapter).filter().all()
    session.commit()
    answer = []
    for i in chapters:
        answer.append({"chapter_id": i.id, 'title': i.name})
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
        answer[-1]['passed_tests'] = passed_tests
        answer[-1]['tests_count'] = tests_count
        answer[-1]['chapter_score'] = chapter_score
        answer[-1]['description'] = i.description
        answer[-1]['img_src'] = i.source_url
    return answer


if __name__ == "__main__":
    app.run(debug=True)
