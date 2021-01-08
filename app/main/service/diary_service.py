import datetime

from app.main import db
from app.main.model.diary import Diary
from .auth_helper import Auth




def save_new_diary(request):

    resp = Auth.get_user_id_with_token(request)
    data = request.json
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    today_diary = Diary.query.filter(Diary.user_id==resp).filter(Diary.created_at==today).first()

    if not today_diary:
        new_diary = Diary (
            user_id=resp,
            context=data['context'],
            emotion=data['emotion'],
            value=data['value']
        )
        
        try:
            save_changes(new_diary)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': e
            }    
            return response_object, 400

        response_object = {
            'status': 'success',
            'message':'Successfully created.'
        }
        return response_object, 201
    else :
        response_object = {
            'status': 'fail',
            'message': 'Today diary already exists. Try tomorrow'
        }
        return response_object,409
    

def get_all_diaries(request,year,month):
    resp = Auth.get_user_id_with_token(request)
    if year != None and month != None:
        start = str(year) + "-" + str(month).zfill(2) + "-01"
        end = str(year) + "-" + str(int(month)+1).zfill(2) + "-01"
        return Diary.query.filter(Diary.user_id==resp).filter(Diary.created_at.between(start,end)).all()
    elif year != None and month == None:
        start = str(year) +"-01-01"
        end = str(int(year)+1) + "-01-01"
        return Diary.query.filter(Diary.user_id==resp).filter(Diary.created_at.between(start,end)).all()
    return Diary.query.filter_by(user_id=resp).all()


def get_a_diary(request,id):

    diary = Diary.query.filter(Diary.id == id).first()
    if diary.user_id != Auth.get_user_id_with_token(request):
        response = {
            'status':'fail',
            'message': "You don't have permission on this object"
        }
        return response,403

    return diary,200

def delete_diary(request,id):
    resp = Auth.get_user_id_with_token(request)
    diary = Diary.query.filter(Diary.id == id).filter(Diary.user_id == resp).first()
    if diary:
        db.session.delete(diary)
        db.session.commit()
    else:
        response = {
            'status':'fail',
            'message':'This diary does not exists'
        }
        return response,404
  
    response = {
        'status':'success',
        'message':'Successfully delete diary'
    }
    return response, 200


def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)