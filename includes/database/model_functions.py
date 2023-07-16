from sqlalchemy.orm import Session

from includes.database.interface import engine
from includes.database.models import User, Game


def create_game(id: str) -> None:
    with Session(engine) as session:
        game: Game = Game(
            id=id,
        )
        session.add_all([game])
        session.commit()



def create_user(id: str, game_id: str, name: str) -> None:
    with Session(engine) as session:
        game: Game = session.query(Game).filter_by(id=game_id).first()
        user: User = User(
            id=id,
            game_id=game.id,
            name=name,
        )
        session.add_all([user])
        session.commit()
