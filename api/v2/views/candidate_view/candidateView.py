from flask import Blueprint,request,jsonify
from api.v2.models.candidate_model.candidateModel import candidates
from api.v2.views.auth_view.user_view import token_required

candidate_bp=Blueprint('candidate',__name__,url_prefix='/api/v2')

@candidate_bp.route('office/<int:office_id>/register',methods=['POST'])
@token_required
def candidate(resp,office_id):
    if resp[9]==False:
        return jsonify({"message":"you are not the admin"})
    data=request.get_json()
    result=candidates(data,office_id).registerCandidate()
    if result['status'] == False:
        return jsonify({"error":result['message']})
    
    candidate={'office':office_id,"user":data['user_id']}
    return jsonify({"data":candidate})