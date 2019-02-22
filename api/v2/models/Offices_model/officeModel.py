from api.v2.utilities.validations.validation import isValid
from api.databaseConfig import connection
class office:
    def __init__(self,data):
        self.data=data
    def addoffice(self):
        data=self.data
        tableName="offices"
        resp=isValid().validate(data,tableName)
        if resp ==True:
            conn=connection()
            cur=conn.cursor()
            try:
                cur.execute("""INSERT INTO office(name,type)
                VALUES (%s,%s);""",(data['name'],data['type']))
                conn.commit()
               
            except:
                conn.rollback()
                return "database requires unique data"
            
            return resp

        return resp