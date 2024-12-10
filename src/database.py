from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_USER, DB_PORT

DATA_BASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATA_BASE_URL, echo=True)

session_maker = sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


def get_session() -> Session:
    with session_maker() as session:
        return session


if __name__ == "__main__":
    from src.model.auth.models import *

    session = get_session()
    version = session.execute(text("SELECT version();"))
    print(version)

    Base.metadata.create_all(bind=engine)
