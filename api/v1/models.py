from flask import Flask

app=Flask(__name__)
PARTIES_DATA=[]

class createParty:
    def __init__(self,name,hqAddress,logoUrl):
        self.id=len(PARTIES_DATA)+1
        self.name=name
        self.hqAddress=hqAddress
        self.logoUrl=logoUrl
    def parties(self):
        PARTIES_DATA.append(self)
        app.logger.info(PARTIES_DATA)

        

        



