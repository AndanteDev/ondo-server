import uuid

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

    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    context = db.Column(db.Text)
    emotion = db.Column(db.Enum(Emotion))
    value = db.Column(db.Float)
    created_at = db.Column(db.Date, nullable=False)

    def __init__(self,user_id,context,emotion,value):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.context = context
        self.emotion = emotion
        self.value = value
        self.created_at = datetime.datetime.today()
        

    def __repr__(self):
        return "<Diary '{}'>".format(self.id)