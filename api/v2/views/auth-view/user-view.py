from flask import Flask,jsonify,request,Blueprint

v2_bp=Blueprint('apiv2', __name__, url_prefix='/api/v2')