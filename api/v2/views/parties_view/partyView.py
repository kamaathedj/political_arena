from flask import request,jsonify,Blueprint
from api.v2.models.Parties_model.partyModel import parties,getpartys
from api.v2.utilities.validations.messages import message
from api.v2.views.auth_view.user_view import token_required
import json
import ast

v2_bp = Blueprint('party', __name__,url_prefix='/api/v2')

@v2_bp.route('/parties',methods=['POST'])
@token_required
def party(resp):
    data=request.get_json(force=True)
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=parties(datadict).addParty()
    return jsonify({"message":resp})

@v2_bp.route('/parties',methods=['GET'])
@token_required
def getparties(resp):
    result=getpartys().getParties()
    mlist=[]
    for re in result:
        mydict={"id":re[0],"name":re[1],"logoUrl":re[2]}
        mlist.append(mydict)
    return jsonify({"status":200,"data":mlist}),200


@v2_bp.route('/parties/<int:id>',methods=['GET'])
def getspecificparty(id):
    result=getpartys().getparty(id)
    if result:
        mlist=[]
        mydict={"id":result[0],"name":result[1],"logoUrl":result[2]}
        mlist.append(mydict)
        return jsonify({"status":200,"data":mlist}),200
    else:
        return 
        


@v2_bp.route('/parties/<int:id>/name',methods=['PATCH'])
def getspecificpartyandpatch(id,name="name"):
    result=getpartys().getpartyandpatch(id,name)
    return jsonify({"message":result})




@v2_bp.route('/parties/<int:id>',methods=['DELETE'])
def deleteparty(id):
    result=getpartys().deleteparty(id)
    mydict={"message":result}
    mlist=[]
    mlist.append(mydict)

    return jsonify({"status":200,"data":mlist})

