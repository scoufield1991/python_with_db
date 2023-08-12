from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

engine = create_engine("postgresql://postgres:123@localhost/mystore", echo=True)

__session = sessionmaker(engine)

session: Session = __session()


