
from flask import jsonify,request,Blueprint,make_response
from werkzeug.security import check_password_hash
from api.v2.models.authentication_model.userModel import user,log
from flask import current_app
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
            data=jwt.decode(token,current_app.config['SECRET_KEY'])
            resp=log().fortoken(data['id'])
        except:
            return jsonify({"message":"token invalid or expired"}),401
        return f(resp,*args,**kwargs)
    return decorated



bp_user = Blueprint('users', __name__,url_prefix='/auth')

@bp_user.route('/signup', methods=['POST'])
@token_required
def createUser(resp):
    print(resp[1])
    data=request.get_json()
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=user(datadict).createUser()
    return jsonify({"message":resp}),201

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
        token=jwt.encode(payload,current_app.config['SECRET_KEY'], algorithm='HS256')
        decoded=token.decode()
        mlist=[]
        mdict={}
        mdict={'id':resp[0],'firstname':resp[1],'lastname':resp[2],'othernames':resp[3],
        'username':resp[4],'email':resp[5],'phone number':resp[6],'password':resp[7],
        'passport url':resp[8],'is admin':resp[9],"token":decoded}
        mlist.append(mdict)
        
        return jsonify({"data":mlist,'status':200}),200
     
        
    return make_response('could not verify',401,{'WWW.Authenticate': 'Basic realm="Login required!"'})

@bp_user.route('/users',methods=['GET'])
def getUsers():
    resp=log().getAllUsers()
    if not resp:
        return jsonify({"Error":"there are no users in the database"})

    mlist=[]
    mdict={}
    for r in resp:
        mdict={'id':r[0],'firstname':r[1],'lastname':r[2],'othernames':r[3],
        'username':r[4],'email':r[5],'phone number':r[6],'password':r[7],
        'passport url':r[8],'is admin':r[9]}
        mlist.append(mdict)
    return jsonify({"data":mlist,"status":200}),200