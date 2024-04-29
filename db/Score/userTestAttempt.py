import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class UserTestAttempt(SqlAlchemyBase):
    __tablename__ = 'userTestAttempts'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("users.id"))
    test_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("chapterTests.id"))
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    right_percent = sqlalchemy.Column(sqlalchemy.DOUBLE)

    user = orm.relationship('User')
    test = orm.relationship('ChapterTest')