from flask import Blueprint,request,jsonify
from api.v2.models.candidate_model.candidateModel import candidates

candidate_bp=Blueprint('candidate',__name__,url_prefix='/api/v2')

@candidate_bp.route('office/<int:office_id>/register',methods=['POST'])
def candidate(office_id):
    user_id=request.get_json()
    result=candidates(user_id).registerCandidate()
    if result == False:
        return jsonify({"error":"no user with that id passed"})
    candidate={'office':office_id,"user":user_id['user']}
    return jsonify({"data":candidate})