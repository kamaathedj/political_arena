from api.databaseConfig import connection
from api.v2.utilities.validations.validation import validate

class candidates:
    def __init__(self,user_id,office_id):
        self.user=user_id
        self.office=office_id

    def registerCandidate(self):
        conn=connection()
        cur=conn.cursor()
        data=self.user
        tableName="candidate"
        id=self.user.get('user_id')
        party=self.user.get('party_id')

        data2={"party_id":party,"user_id":id,"office_id":self.office}
        response=validate(data2,tableName)
        if response['isvalid'] is False:
            return{
                'status':False,
                'message':response['message']

            }
        try:
            id=self.user.get('user_id')
            party_id=self.user.get('party_id')
            print(self.office)
            
            cur.execute("""INSERT INTO candidate(office_id,candidate_id,party_id)
            VALUES (%s,%s,%s);""",(self.office,id,party_id))
            conn.commit()
            return{
                'status':True
            }
        except:
            message='error occured when inserting into the database please make sure that the party_id,user_id are correct'
            return {
                'status':False,
                'message':message   
            }
class getting:
    def getCandidates(self):
        conn=connection()
        cur=conn.cursor()
        try:
            cur.execute("""SELECT * FROM candidate""")
            data=cur.fetchall()
            return data
        except :
            return 'error from db'
        
      