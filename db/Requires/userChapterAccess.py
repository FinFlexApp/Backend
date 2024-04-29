import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class UserChapterAccess(SqlAlchemyBase):
    __tablename__ = 'userChapterAccesses'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("users.id"))
    chapter_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapters.id"))
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    user = orm.relationship("User")
    chapter = orm.relationship("Chapter")