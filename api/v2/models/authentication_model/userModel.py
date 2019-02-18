from api.v2.utilities.validations.validation import isValid
class user():
    def __init__(self,data=None):
        self.resp=data
    def createUser(self):
        response=isValid().validate(self.resp)
        return response
