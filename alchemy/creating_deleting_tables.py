from utilities.base import Base
from utilities.session_db import engine


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Create tables")


def drop_tables():
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped.")
