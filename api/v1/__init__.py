from api.config import app_configurations
from api.v1.views import userbp
from flask import Flask

def creating_app(enviroment):
    app=Flask(__name__)
    app.config.from_object(app_configurations[enviroment])
    app.register_blueprint(userbp)
    return app

