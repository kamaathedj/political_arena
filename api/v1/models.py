from flask import Flask

app=Flask(__name__)
PARTIES_DATA=[]


class createParty:
    def __init__(self,id,name,hqAddress,logoUrl):
        self.id=id
        self.name=name
        self.hqAddress=hqAddress
        self.logoUrl=logoUrl

  
        
    # def parties(self):
    #     app.logger.info(PARTIES_DATA)
    #     return PARTIES_DATA


def getPartyId(id):
    party_loop=None
    for party in PARTIES_DATA:
        if party.id==id:
            party_loop=party
            break
    return party_loop

   
    
        