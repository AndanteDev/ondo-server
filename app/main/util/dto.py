from flask_restplus import Namespace, fields

class UserDto:
    api = Namespace('user',description='user related operations')
    user = api.model('user', {
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
        'context': fields.String(description='diary context'),
        'emotion': fields.Integer(description='diary emotion'),
        'value': fields.Float(description='diary value of emotion'),
        'created_at' : fields.DateTime(description='diary created at')
    })
    
