from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String, unique=True, nullable=False)
    preferences = Column(JSON)

    def to_dict(self):
        return {
            'id': self.id,
            'discord_id': self.discord_id,
            'preferences': self.preferences
        }

def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    global Session
    Session = sessionmaker(bind=engine)

db = Session()
