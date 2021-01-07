from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user',description='user related operations')
    user = api.model('user', {
        'id':fields.Integer(description='user id'),
        'email':fields.String(required=True,description='user email address'),
        'username':fields.String(required=True,description='user username'),
        'password':fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        'joined_at': fields.DateTime(description='user joined at')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })



class DiaryDto:
    api = Namespace('diary',description='diary related operations')
    diary = api.model('diary',{
        'id':fields.String(description='diary id'),
        'user_id':fields.Integer(description='diary owner id'),
        'context': fields.String(description='diary context'),
        'emotion': fields.Integer(description='diary emotion'),
        'value': fields.Float(description='diary value of emotion'),
        'created_at' : fields.Date(description='diary created at')
    })
    
class EmotionDto:
    api = Namespace('emotion',description='emotion related operations')
    emotion = api.model('emotion',{
        'id':fields.String(description='diary id'),
        'emotion':fields.Integer(description='diary emotion'),
        'value':fields.Float(description='diary value')
    })