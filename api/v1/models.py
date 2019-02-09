from flask import Flask


PARTIES_DATA=[
    {
        "id": 1, 
        "name": "Jubilee",
        "hqAddress":"nairobi",
        "logoUrl":"www.google.com"
    }
]
POLITICAL_OFFICE=[
    {
        "id":1,
        "name":"meme",
        "type":"president"
    }
]


class createParty:
    def __init__(self,id,name,hqAddress,logoUrl):
        self.id=id
        self.name=name
        self.hqAddress=hqAddress
        self.logoUrl=logoUrl

  
        
    # def parties(self):
    #     app.logger.info(PARTIES_DATA)
    #     return PARTIES_DATA


# def getPartyId(id):
#     party_loop=None
#     for party in PARTIES_DATA:
#         if party.id==id:
#             party_loop=party
#             break
#     return party_loop

   
class createOffice:
    def __init__(self,id,name,type):
        self.id=id
        self.name=name
        self.type=type

  