import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class QuestionAnswer(SqlAlchemyBase):
    __tablename__ = 'questionAnswers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    question_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("testQuestions.id"))
    text = sqlalchemy.Column(sqlalchemy.Text)
    isRight = sqlalchemy.Column(sqlalchemy.Boolean)
    img_src = sqlalchemy.Column(sqlalchemy.String)
    testQuestion = orm.relationship('TestQuestion')