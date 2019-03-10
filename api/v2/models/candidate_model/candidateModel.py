from api.databaseConfig import connection

class candidates:
    def __init__(self,user):
        self.user=user

    def registerCandidate(self):
        conn=connection()
        cur=conn.cursor()
        try:
            id=self.user.get('user')
            cur.execute("""SELECT * FROM user_table WHERE id=%s""",[id])
            result=cur.fetchone()
            if not result:
                return False
            
            return True
        except:
            return False

        