rawDataKeys={
    "user":("firstname", "lastname", "othername","username", "email", "password", "phonenumber", "passporturl", "is_admin"),
}

class isValid:
    def validate(self,data,tableName):
        resp=isValid().validation(data,tableName)
        print(tableName)
        return resp   
    def validation(self,data,tableName):
        if all(y in data for y in rawDataKeys[tableName]):
            resp=isValid().validateValues(data)
            return resp
        else:
            return False
    def validateValues(self,data):
        for x in data:
            if not data[x]:
                return False
        return True