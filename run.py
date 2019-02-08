from flask import Flask
from api.v1 import creating_app

from api.v1.views import create




env="development"
app=creating_app(env)

if __name__=='__main__':
    app.run()