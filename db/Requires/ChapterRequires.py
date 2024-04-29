import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class ChapterRequire(SqlAlchemyBase):
    __tablename__ = 'chapterRequires'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    unlockable_chapter_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapters.id"))
    required_chapter_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapters.id"))
    unlockable_chapter = orm.relationship("Chapter", foreign_keys=[unlockable_chapter_id])
    required_chapter = orm.relationship("Chapter", foreign_keys=[required_chapter_id])
