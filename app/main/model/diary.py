from .. import db,flask_bcrypt
import datetime
import enum
from .user import User

class Emotion(enum.IntEnum):
    happy = 1
    sad = 2
    angry = 3
    soso = 4

class Diary(db.Model):
    __tablename__ = "diary"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    context = db.Column(db.Text)
    emotion = db.Column(db.Enum(Emotion))
    value = db.Column(db.Float)
    created_at = db.Column(db.DateTime, nullable=False)


    def __repr__(self):
        return "<Diary '{}'>".format(self.id)