import datetime

from app.main import db
from app.main.model.diary import Diary
from .auth_helper import Auth




def get_my_emotions(request,year,month):
    resp = Auth.get_user_id_with_token(request)
    if year != None and month != None:
        start = str(year) + "-" + str(month).zfill(2) + "-01"
        end = str(year) + "-" + str(int(month)+1).zfill(2) + "-01"
        return Diary.query(Diary.id,Diary.emotion,Diary.value).filter(Diary.user_id==resp).filter(Diary.created_at.between(start,end)).all()
    elif year != None and month == None:
        start = str(year) +"-01-01"
        end = str(int(year)+1) + "-01-01"
        return Diary.query(Diary.id,Diary.emotion,Diary.value).filter(Diary.user_id==resp).filter(Diary.created_at.between(start,end)).all()
    return Diary.query("id").filter(Diary.user_id==resp)[-30:]


