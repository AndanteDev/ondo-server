import datetime

from app.main import db
from app.main.model.diary import Diary
from .auth_helper import Auth


def save_new_diary(request):
    data = request.json
    resp = Auth.get_user_id_with_token(request)

    new_diary = Diary (
        context = data['context'],
        user_id = resp,
        emotion = data['emotion'],
        value = data['value'],
        created_at = datetime.datetime.utcnow
    )
    
    try:
        save_changes(new_diary)
    except e:
        response_object = {
            'status': 'fail',
            'message': e
        }    
        return response_object, 400

    response_object = {
        'status': 'success',
        'message':'Successfully registered.'
    }
    return response_object, 201

    

def get_all_diaries(request):
    resp = Auth.get_user_id_with_token(request)
    return Diary.query.filter_by(user_id=resp)


def get_a_diary(request,id):

    diary = Diary.query.filter_by(id=id).first()
    if diary.user_id != Auth.get_user_id_with_token(request):
        response_object = {
            'status':'fail',
            'message': "You don't have permission on this object"
        }
        return response_object

    return diary


def save_changes(data):
    db.session.add(data)
    db.session.commit()
