import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class Chapter(SqlAlchemyBase):
    __tablename__ = 'chapters'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    sequence = sqlalchemy.Column(sqlalchemy.Integer)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.Text)
    source_url = sqlalchemy.Column(sqlalchemy.String)

    chapterTests = orm.relationship("ChapterTest", backref='chapters')