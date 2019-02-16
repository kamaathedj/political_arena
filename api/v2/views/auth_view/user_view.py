from flask import jsonify,request,Blueprint

v2_bp = Blueprint('apiv2', __name__, url_prefix='/api/v2')

@v2_bp.route('/users', methods=['POST'])
def createUser():
    return jsonify({"message":"time to start v2"})