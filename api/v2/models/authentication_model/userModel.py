from werkzeug.security import generate_password_hash
from api.databaseConfig import connection
from api.v2.utilities.validations.validation import validate
from api.v2.utilities.url_validate import url
class user():
    def __init__(self,data=None):
        self.resp=data
    def createUser(self):
        data=self.resp
        tableName="user"
        response=validate(data,tableName)
        password=generate_password_hash(data['password'],"sha256")
        print(password)
        response_url=url(data['passporturl']).validateUrl()
        if response['isvalid']is False:
            return response["message"]
        if response_url is True:
            conn=connection()
            cur=conn.cursor()
            try:
                cur.execute("""INSERT INTO user_table(firstname,lastname,othernames,username,email,password,phonenumber,passporturl,isadmin)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);""",(data['firstname'],data['lastname'],data['othername'],data['username'],data['email'],
                password,data['phonenumber'],data['passporturl'],data['is_admin']))
                conn.commit()
                
            except:
                conn.rollback()
                return "database requires unique data"
            
            return response


class log:
    def login(self,data):
        return "implement this login functionality"

        

