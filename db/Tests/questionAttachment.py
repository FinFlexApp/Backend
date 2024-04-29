import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class QuestionAttachment(SqlAlchemyBase):
    __tablename__ = 'questionAttachments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    question_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("testQuestions.id"))
    media_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("mediaTypes.id"))
    source_url = sqlalchemy.Column(sqlalchemy.String)
    testQuestion = orm.relationship('TestQuestion')
    mediaType = orm.relationship('MediaType')
