from instance.config import app_configurations
from api.v1.views import userbp
from api.v2.views.auth_view.user_view import v2_bp
from flask import Flask,jsonify
from api.v1.models import createParty

def methodNotAllowed(error):
    return jsonify({
        "error": str(error),
        "status":405
    }),405

def pageNotFound(error):
    return jsonify({
        "error": str(error),
        "status":404
    }),404
def badRequest(error):
    return jsonify({
        "error": str(error),
        "status":400
    }),400
    


def creating_app():
    app=Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_configurations["development"])
    app.register_blueprint(userbp)
    app.register_blueprint(v2_bp)
    app.register_error_handler(405,methodNotAllowed)
    app.register_error_handler(404,pageNotFound)
    app.register_error_handler(400,badRequest)
    return app

