from functools import wraps
import jwt
from flask import request, abort
from flask import current_app
from db.user import User
from db import db_session

db_session.global_init("db/users.db")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        session = db_session.create_session()
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = session.query(User).get(data['user_id'])
            session.commit()
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated
