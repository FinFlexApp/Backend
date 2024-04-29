import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class ChapterTest(SqlAlchemyBase):
    __tablename__ = 'chapterTests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    chapter_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("chapters.id"))
    sequence = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.Text)
    chapter = orm.relationship('Chapter')

    testQuestions = orm.relationship("TestQuestion", backref='chapterTests')
    userTestAttempts = orm.relationship("UserTestAttempt", backref='chapterTests')
    testScore = orm.relationship("TestScore", backref='chapterTests')
    testAttachments = orm.relationship("TestAttachment", backref='chapterTests')
