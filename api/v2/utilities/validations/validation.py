import string
rawDataKeys={
    "user":("firstname", "lastname", "othername","username", "email", "password", "phonenumber", "passporturl", "is_admin"),
    "offices":("name","type"),
    "parties":("name","hqAddress","logoUrl")
}



 
def validation(data,tableName):
    if all(y in data for y in rawDataKeys[tableName]):
        return True
    else:
        return False
def validateValues(data):
    for x in data:
        if not data[x]:
            return False
    return True
def nowhitespaces(data):
    for x in data:
        if isinstance(data[x],str):
            if data[x].isspace():
                return True
        else:
            return False


def validate(data,tableName):
    if validation(data,tableName) is False:
        return {
            "isvalid":False,
            "message":"Please make sure to enter the correct response"+ str(rawDataKeys[tableName])
        }
        
    if validateValues(data) is False:
        return{
            "isvalid":False,
            "message":"Please make sure to enter the correct values"+str(rawDataKeys[tableName])
        }
    if nowhitespaces(data) is True:
        return {
            "isvalid": False,
            "message":"Please make sure the values do not have whitespaces"
        }
    return{

        "isvalid":True
    }

    

   