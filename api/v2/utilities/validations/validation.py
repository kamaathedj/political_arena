rawDataKeys={
    "user":("firstname", "lastname", "othername", "email", "password", "phonenumber", "passporturl", "is_admin"),
}

class isValid:
    def validate(self,data):
        resp=isValid().validation(data)
        return resp   
    def validation(self,data):
        if all(y in data for y in rawDataKeys["user"]):
            return True
        else:
            return False


        

   