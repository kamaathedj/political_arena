from flask import jsonify,Blueprint,request
from api.v2.models.Offices_model.officeModel import office,getOffices
from api.v2.views.auth_view.user_view import token_required
import json
import ast

office_bp = Blueprint('apiv2', __name__, url_prefix='/api/v2')

@office_bp.route('/offices',methods=['POST'])
@token_required
def offices(resp):
    data=request.get_json(force=True)
    data_json=json.dumps(data)
    datadict=ast.literal_eval(data_json)
    resp=office(datadict).addoffice()
    mlist=[]
    mlist.append(resp)
    return jsonify({"status":200,"message":mlist}),200

@office_bp.route('/offices',methods=['GET'])
@token_required
def AllOffices(resp):
    resp=getOffices().GetAllOffices()
    mlist=[]
    mdict={}
    if not resp:
        return jsonify({"message":'There are no offices'})
    for r in resp:
        mdict={'id':r[0],'name':r[1],'type':r[2]}
        mlist.append(mdict)

    return jsonify({"message":mlist,'status':200}),200



@office_bp.route('/offices/<int:id>',methods=['GET'])
def SpecificOffices(id):
    resp=getOffices().GetSpecificOffices(id)
    mlist=[]
    mdict={}
    if not resp:
        return jsonify({"error":'There are no office with that id',"status":404}),404

    mdict={'id':resp[0],'name':resp[1],'type':resp[2]}
    mlist.append(mdict)

    return jsonify({"data":mlist,'status':200}),200


