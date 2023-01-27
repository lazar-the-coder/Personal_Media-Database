from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


engine = create_engine('sqlite:///media.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    title = Column("Title", String)
    writer = Column("Writer", String)
    visionary = Column("Visionary", String)
    date = Column("Published", Date)
    medium = Column("Medium", String)
    status = Column("Status", String)
    genre = Column("Genres", String)
    
    def __repr__(self):
        return f'*Presently {self.status} *{self.title}*, a *{self.medium}* written by *{self.writer}* and visualized by *{self.visionary}*, written *{self.date}*, in these genres: {self.genre}.'