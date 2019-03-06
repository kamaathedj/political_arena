from flask import jsonify,request,Blueprint,make_response
from werkzeug.security import check_password_hash
from api.v2.models.authentication_model.userModel import user,log
from functools import wraps
import ast
import json
import datetime
import os
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        if not token:
            return jsonify({"message":"token is missing"}),401
        try:
            data=jwt.decode(token,os.getenv('FLASK_SECRET'))
            resp=log().fortoken(data['id'])
            print(resp)
        except:
            return jsonify({"message":"token invalid"}),401
        return f(resp,*args,**kwargs)
    return decorated



bp_user = Blueprint('users', __name__,url_prefix='/api/v2')

@bp_user.route('/users', methods=['POST'])
@token_required
def createUser(resp):
    data=request.get_json()
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=user(datadict).createUser()
    return jsonify({"message":resp})

@bp_user.route('/login',methods=['GET'])
def login():
    auth=request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('could not verify',401,{'WWW.Authenticate': 'Basic realm="Login required!"'})
    resp=log().login(auth.username)
    dbpass=resp[7]
    if not resp:
        return make_response('could not verify',401,{'WWW.Authenticate': 'Basic realm="Login required!"'})
    if check_password_hash(dbpass,auth.password):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'id': resp[0]
        }
        token=jwt.encode(payload,os.getenv('FLASK_SECRET'), algorithm='HS256')
        decoded=token.decode()
        return jsonify({"token":decoded})
     
        
    return make_response('could not verify',401,{'WWW.Authenticate': 'Basic realm="Login required!"'})