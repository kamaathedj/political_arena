from api.databaseConfig import connection

class candidates:
    def __init__(self,user_id,office_id):
        self.user=user_id
        self.office=office_id

    def registerCandidate(self):
        conn=connection()
        cur=conn.cursor()
       
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

        