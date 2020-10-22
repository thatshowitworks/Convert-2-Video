from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sample_config import Config

DB_URI = Config.DB_URI


def start() -> scoped_session:
    """ returns SQLAlchemy ScopedSession """
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(
        sessionmaker(
            bind=engine,
            autoflush=False
        )
    )


BASE = declarative_base()
SESSION = start()