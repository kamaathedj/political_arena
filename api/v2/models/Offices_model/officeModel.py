from api.v2.utilities.validations.validation import validate
from api.databaseConfig import connection
class office:
    def __init__(self,data):
        self.data=data
    def addoffice(self):
        data=self.data
        tableName="offices"
        resp=validate(data,tableName)
        if resp['isvalid'] is False :
            return resp["message"]
        
        conn=connection()
        cur=conn.cursor()
        try:
            cur.execute("""INSERT INTO office(name,type)
            VALUES (%s,%s);""",(data['name'],data['type']))
            conn.commit()
            
        except:
            conn.rollback()
            return "database requires unique data"
        
        return data

            