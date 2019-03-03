from api.v2.utilities.validations.validation import validate
from api.v2.utilities.url_validate import url
from api.databaseConfig import connection
from api.v2.utilities.validations.messages import message
class parties:
    def __init__(self,data):
        self.data=data
    def addParty(self):
        tableName="parties"
        data=self.data
        resp=validate(data,tableName)
        emailResponse=url(data['logoUrl']).validateUrl()
        
        if resp["isvalid"] is  False:
            return resp["message"]
        elif emailResponse==True :
            conn=connection()
            cur=conn.cursor()
            try:
                cur.execute("""INSERT INTO party(name,hqAddress,logoUrl)
                VALUES (%s,%s,%s);""",(data['name'],data['hqAddress'],data['logoUrl']))
                conn.commit()
                return "succesful"
                
            except:
                conn.rollback()
                return "database requires unique data"
            
            return resp

        
    

class getpartys:
    
    def getParties(self):
        conn=connection()
        cur=conn.cursor()
        try:
            cur.execute("""SELECT * FROM party""")
            resp=cur.fetchall()
            return resp 
        except :
            return "error"
        
    def getparty(self,id):
        try:
            conn=connection()
            cur=conn.cursor()
            cur.execute("""SELECT * FROM party WHERE id=%s""",[id])
            result=cur.fetchone()
            if result:   
                return result
            else:
                message("error occured").error()
        except:
            return False
    

    def getpartyandpatch(self,id,name):
            try:
                conn=connection()
                cur=conn.cursor()
                cur.execute("""SELECT * FROM party WHERE id=%s""",[id])
                party=cur.fetchone()
                
                return party
            except:
                return "error"
    def deleteparty(self,id):
            try:
                conn=connection()
                cur=conn.cursor()
                result=cur.execute("""DELETE FROM party WHERE id=%s""",[id])
                conn.commit()
                return "party deleted"
            except:
                return "error deleting non existing party"


