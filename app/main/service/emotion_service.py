import datetime

from app.main import db
from app.main.model.diary import Diary
from .auth_helper import Auth



def get_my_emotions(request,year,month):
    resp = Auth.get_user_id_with_token(request)

    result = Diary.query(Diary.id,Diary.emotion,Diary.value).filter(Diary.user_id == resp).all()
    return result