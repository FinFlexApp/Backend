import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class TestQuestion(SqlAlchemyBase):
    __tablename__ = 'testQuestions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    test_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("chapterTests.id"))
    sequence = sqlalchemy.Column(sqlalchemy.Integer)
    text = sqlalchemy.Column(sqlalchemy.Text)
    img_src = sqlalchemy.Column(sqlalchemy.String)
    multiple_choice = sqlalchemy.Column(sqlalchemy.Boolean)
    chapterTest = orm.relationship('ChapterTest')
    questionAnswers = orm.relationship("QuestionAnswer", backref='testQuestions')
