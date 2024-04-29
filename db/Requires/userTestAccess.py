import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class UserTestAccess(SqlAlchemyBase):
    __tablename__ = 'userTestAccesses'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("users.id"))
    test_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapterTests.id"))
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    user = orm.relationship("User")
    chapter = orm.relationship("ChapterTest")
