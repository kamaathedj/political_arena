from instance.config import app_configurations
from api.v1.views import userbp
from api.v2.views import v2_bp
from flask import Flask
from api.v1.models import createParty

def creating_app(enviroment):
    app=Flask(__name__)
    app.config.from_object(app_configurations[enviroment])
    app.register_blueprint(userbp)
    app.register_blueprint(v2_bp)
    return app
