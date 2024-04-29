import sqlalchemy
from db.db_session import SqlAlchemyBase
from sqlalchemy import orm

class ChatBotHistory(SqlAlchemyBase):
    __tablename__ = 'chatBotHistories'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.INTEGER, sqlalchemy.ForeignKey("users.id"))
    text = sqlalchemy.Column(sqlalchemy.TEXT)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    isReplay = sqlalchemy.Column(sqlalchemy.Boolean)

    user = orm.relationship('User')