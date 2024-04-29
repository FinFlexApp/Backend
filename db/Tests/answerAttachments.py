import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class AnswerAttachment(SqlAlchemyBase):
    __tablename__ = 'answerAttachments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    answer_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("questionAnswers.id"))
    media_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("mediaTypes.id"))
    source_url = sqlalchemy.Column(sqlalchemy.String)
    testQuestion = orm.relationship('QuestionAnswer')
    mediaType = orm.relationship('MediaType')
