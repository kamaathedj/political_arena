from flask import jsonify,Blueprint,request
from api.v2.models.Offices_model.officeModel import office
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