import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class LeaderBoard(SqlAlchemyBase):
    __tablename__ = 'leaderBoards'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("users.id"))
    score = sqlalchemy.Column(sqlalchemy.INTEGER)
    tests_passed = sqlalchemy.Column(sqlalchemy.INTEGER)

    user = orm.relationship('User')