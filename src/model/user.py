from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"


engine = create_engine('sqlite:///database.db', echo=True)
Base.metadata.create_all(engine)


def insert_user(username: str, password: str):
    session = sessionmaker(bind=engine)
    session = session()

    new_user = Users(
        username=username,
        password=password
    )
    session.add(new_user)
    session.commit()
    session.close()
