from flask import jsonify,request,Blueprint
from api.v2.models.authentication_model.userModel import user
import ast
import json

v2_bp = Blueprint('apiv2', __name__, url_prefix='/api/v2')

@v2_bp.route('/users', methods=['POST'])
def createUser():
    data=request.get_json(force=True)
    jsodata=json.dumps(data)
    datadict=ast.literal_eval(jsodata)
    resp=user(datadict).createUser()

    return jsonify({"message":"The account was created","message 2":resp})