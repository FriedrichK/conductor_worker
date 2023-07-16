from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Game(Base):
    __tablename__ = 'games'
    id = Column(String, primary_key=True)


class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    game_id = Column(String, ForeignKey('games.id'))
    name = Column(String(32))
