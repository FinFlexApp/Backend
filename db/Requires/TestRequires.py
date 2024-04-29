import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class TestRequire(SqlAlchemyBase):
    __tablename__ = 'testRequires'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    unlockable_test_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapterTests.id"))
    required_test_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("chapterTests.id"))
    unlockable_test = orm.relationship("ChapterTest", foreign_keys=[unlockable_test_id])
    required_test = orm.relationship("ChapterTest", foreign_keys=[required_test_id])