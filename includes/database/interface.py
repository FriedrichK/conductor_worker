import os

import sqlalchemy

from includes import settings
from includes.database.models import Base

db_path: str = os.path.abspath(os.path.join(settings.BASE_PATH, "db.sqlite3"))
engine = sqlalchemy.create_engine(f"sqlite:///{db_path}", echo=True)

Base.metadata.create_all(engine)
