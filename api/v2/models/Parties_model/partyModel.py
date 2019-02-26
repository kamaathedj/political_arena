from api.v2.utilities.validations.validation import isValid
from api.v2.utilities.url_validate import url
from api.databaseConfig import connection
class parties:
    def __init__(self,data):
        self.data=data
    def addParty(self):
        tableName="parties"
        data=self.data
        resp=isValid().validate(data,tableName)
        emailResponse=url(data['logoUrl']).validateUrl()
        if emailResponse==True and resp==True:
            conn=connection()
            cur=conn.cursor()
            try:
                cur.execute("""INSERT INTO party(name,hqAddress,logoUrl)
                VALUES (%s,%s,%s);""",(data['name'],data['hqAddress'],data['logoUrl']))
                conn.commit()
               
            except:
                conn.rollback()
                return "database requires unique data"
            
            return resp

        return emailResponse
