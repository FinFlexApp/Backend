import sqlalchemy
import os
import hashlib
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    nickname = sqlalchemy.Column(sqlalchemy.String)
    firstname = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    img_src = sqlalchemy.Column(sqlalchemy.String)
    reg_date = sqlalchemy.Column(sqlalchemy.DateTime)

    chatBotHistories = orm.relationship("ChatBotHistory", backref='users')
    userTestAttempts = orm.relationship("UserTestAttempt", backref='users')
    leaderBoards = orm.relationship("LeaderBoard", backref='users')
    userChapterAccesses = orm.relationship("UserChapterAccess", backref='users')
    userTestAccesses = orm.relationship("UserTestAccess", backref='users')

    def set_password(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000)
        storage = salt + key
        self.hashed_password = storage

    def check_password(self, password):
        salt_from_storage = self.hashed_password[:32]
        key_from_storage = self.hashed_password[32:]
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt_from_storage,
            100000
        )
        return new_key == key_from_storage
