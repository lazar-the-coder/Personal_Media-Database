from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)


class Piece(db.Model):
    # Any piece
    # Literature, Play
    id = db.Column(db.Integer, primary_key=True)
    # Literature, Play, Illustrated Book, Graphic Novel, Comic Series
    # Live Action Movie, Live Action Series, Animated Movie, Animated Series
    # Video Game
    medium = db.Column("Medium", db.String())
    title = db.Column("Title", db.String())
    writer = db.Column("Writer", db.String())
    released = db.Column("Released", db.DateTime)
    finished = db.Column("Finished", db.DateTime)
    # Plan to View, Currently Viewing, Finished, On Hold, Abandoned
    status = db.Column("Status", db.String())
    # F to A, S for Max
    tier = db.Column("Tier", db.String())
    genre = db.Column("Genres", db.Text)
    description = db.Column("Description", db.Text)
    notes = db.Column("Notes", db.Text)
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* written by *{self.writer}*
                \rpublished *{self.released}*, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rThe story: {self.description}
                \rI think it's {self.tier} tier, {self.notes}
                ''')

class Drawn(Piece):
    # Any piece with writing and visual art
    # Illustrated Literature, Graphic Novel, Comic Series
    artist = db.Column("Artist", db.String())
    publisher  = db.Column("Publisher", db.String())
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* with *{self.writer}* as writer and *{self.artist}* as artist
                \rpublished *{self.released}* by {self.publisher}, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rThe story: {self.description}
                \rI think it's {self.tier} tier, {self.notes}
                ''')

class Film(Piece):
    # Any piece with motion picture
    # Movie, Series
    director = db.Column("Director", db.String())
    actors = db.Column("Actors", db.Text)
    producer = db.Column("Producer", db.String())
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* written by *{self.writer}* and directed by *{self.director}*
                \rreleased *{self.released}* by {self.producer}, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rhere are some of the actors are: {self.actors}
                \rThe story: {self.description}
                \rI think it's {self.tier} tier, {self.notes}
                ''')

class Animation(Film):
    # Any piece with motion picture with animation
    # Movie, Series
    animator = db.Column("Animator", db.String())
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* written by *{self.writer}*, directed by *{self.director}*, and animated by *{self.animator}*
                \rreleased *{self.released}* by {self.producer}, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rhere are some of the actors are: {self.actors}
                \rThe story: {self.description}
                \rI think it's {self.tier} tier, {self.notes}
                ''')

class Game(Piece):
    # Any video game
    designers = db.Column("Designer", db.Text)
    developer = db.Column("Developer", db.String())
    gameplay = db.Column("Gameplay", db.Text)
    
    def __repr__(self):
        return (f'''
                \r*Presently {self.status} *{self.title}*
                \rA *{self.medium}* written by *{self.writer}*, with major designers *{self.designers}* 
                \rreleased *{self.released}* by {self.developer}, I finished it *{self.finished}*
                \rin these genres: {self.genre}
                \rThe story: {self.description}
                \rThe gameplay: {self.gameplay}
                \rI think it's {self.tier} tier, {self.notes}
                ''')