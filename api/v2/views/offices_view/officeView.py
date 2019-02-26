from flask import jsonify,Blueprint,request
from api.v2.models.Offices_model.officeModel import office

office_bp = Blueprint('apiv2', __name__, url_prefix='/api/v2')

@office_bp.route('/offices',methods=['POST'])
def offices():
    resp=office(request.get_json(force=True)).addoffice()
    return jsonify({"message":resp}),200