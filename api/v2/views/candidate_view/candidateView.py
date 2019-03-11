from flask import Blueprint,request,jsonify
from api.v2.models.candidate_model.candidateModel import candidates

candidate_bp=Blueprint('candidate',__name__,url_prefix='/api/v2')

@candidate_bp.route('office/<int:office_id>/register',methods=['POST'])
def candidate(office_id):
    data=request.get_json()
    result=candidates(data,office_id).registerCandidate()
    if result['status'] == False:
        return jsonify({"error":result['message']})
    
    candidate={'office':office_id,"user":data['user_id']}
    return jsonify({"data":candidate})