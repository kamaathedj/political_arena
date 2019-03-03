from flask import jsonify,request,Blueprint
from api.v2.models.authentication_model.userModel import user,log
import ast
import json

bp_user = Blueprint('users', __name__,url_prefix='/api/v2')

@bp_user.route('/users', methods=['POST'])
def createUser():
    data=request.get_json()
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=user(datadict).createUser()
    return jsonify({"message":resp})

@bp_user.route('/users',methods=['GET'])
def login():
    data=request.get_json()
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=log().login(datadict)
    return jsonify({"message":"data is being matched","message2":resp})