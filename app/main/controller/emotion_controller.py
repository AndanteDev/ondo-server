from flask import request
from flask_restplus import Resource

from ..util.dto import EmotionDto
from ..service.emotion_service import *

from app.main.util.decorator import token_required

api = EmotionDto.api
_emotion = EmotionDto.emotion

@api.route('/')
class EmotionList(Resource):
    @token_required
    @api.doc('list_of_my_emotions')
    @api.marshal_list_with(_emotion,envelope='data')
    @api.doc(params={'year': {'description': 'emotion year',
                                'type': 'string', 'required':False},
                    'month': {'description': 'emotion month',
                                'type': 'string', 'required':False}})
    def get(self):
        year = request.args.get('year')
        month = request.args.get('month')
        return get_my_emotions(request=request,year = year,month=month)



        