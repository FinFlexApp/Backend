import sqlalchemy
from sqlalchemy import orm
from db.db_session import SqlAlchemyBase


class MediaType(SqlAlchemyBase):
    __tablename__ = 'mediaTypes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.Text)