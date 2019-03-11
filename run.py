from api import creating_app
from api.databaseConfig import CreateTable


app=creating_app()
CreateTable()

if __name__=='__main__':
    app.run()