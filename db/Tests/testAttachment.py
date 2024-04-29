import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class TestAttachment(SqlAlchemyBase):
    __tablename__ = 'testAttachments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    test_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("chapterTests.id"))
    media_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("mediaTypes.id"))
    source_url = sqlalchemy.Column(sqlalchemy.String)
    chapterTest = orm.relationship('ChapterTest')
    mediaType = orm.relationship('MediaType')