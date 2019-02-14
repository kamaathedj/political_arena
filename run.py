from api import creating_app
from api.v1.views import create
import os

app=creating_app(os.getenv('FLASK_ENV'))

if __name__=='__main__':
    app.run()