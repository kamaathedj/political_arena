from flask import request,jsonify,Blueprint
from api.v2.models.Parties_model.partyModel import parties
# from api.v2.views import v2_bp

v2_bp = Blueprint('party', __name__,url_prefix='/api/v2')

@v2_bp.route('/parties',methods=['POST'])
def party():
    data=request.get_json(force=True)
    resp=parties(data).addParty()
    return jsonify({"message":resp})