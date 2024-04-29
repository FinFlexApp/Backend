import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class TestScore(SqlAlchemyBase):
    __tablename__ = 'testScores'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    test_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapterTests.id"))
    max_score = sqlalchemy.Column(sqlalchemy.Integer)

    test = orm.relationship('ChapterTest')