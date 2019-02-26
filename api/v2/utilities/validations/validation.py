rawDataKeys={
    "user":("firstname", "lastname", "othername","username", "email", "password", "phonenumber", "passporturl", "is_admin"),
    "offices":("name","type"),
    "parties":("name","hqAddress","logoUrl")
}

class isValid:
    def validate(self,data,tableName):
        resp=isValid().validation(data,tableName)
        return resp   
    def validation(self,data,tableName):
        if all(y in data for y in rawDataKeys[tableName]):
            resp=isValid().validateValues(data)
            print(resp)
            return resp
        else:
            return False
    def validateValues(self,data):
        for x in data:
            if not data[x]:
                return False
        return True