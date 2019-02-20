from api import creating_app
from api.databaseConfig import CreateTable
from api.v1.views import create
import os

app=creating_app()
CreateTable()

if __name__=='__main__':
    app.run()