from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from insidegrid.settings import settings

engine = create_engine(settings.POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as exc:
        db.rollback()
        raise exc
    finally:
        db.close()
