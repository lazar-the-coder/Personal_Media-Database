from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column("Title", db.String())
    writer = db.Column("Writer", db.String())
    visionary = db.Column("Visionary", db.String())
    published = db.Column("Published", db.DateTime)
    finished = db.Column("Finished", db.DateTime)
    medium = db.Column("Medium", db.String())
    status = db.Column("Status", db.String())
    tier = db.Column("Tier", db.String())
    genre = db.Column("Genres", db.Text)
    notes = db.Column("Notes", db.Text)
    description = db.Column("Description", db.Text)
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* written by *{self.writer}* and visualized by *{self.visionary}*
                \rwritten *{self.published}*, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rThe story: {self.description}
                \rI think it's {self.tier} tier, {self.notes}
                ''')