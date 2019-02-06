from api.v1.models import PARTIES_DATA
import random


from flask import Flask,jsonify,request,logging,Blueprint,make_response
app=Flask(__name__)

userbp=Blueprint("apiv1",__name__,url_prefix = "/api/v1")


# app.logger.info('kamaa')

@userbp.route('/parties', methods=['POST'])
def create():
    data=request.get_json(force=True)
    # app.logger.info(data)
    
    id=random.randint(5,100)
    name=data['name']
    hqAddress=data['hqAddress']
    logoUrl=data['logoUrl']
    # PARTY.append[data]
#     new_party=createParty(id,name,hqAddress,logoUrl)

    new_party={
            "id":id,
            "name":name,
            "hqAddress":hqAddress,
            "logoUrl":logoUrl
    }
    
    PARTIES_DATA.append(new_party)
    return make_response(jsonify({
            "status":200,
            "party":new_party
    }),200)

@userbp.route('/getparties', methods=['GET'])
def GetParties():
    return jsonify(
        {"status" :200},
        {"parties":PARTIES_DATA})

@userbp.route('/specificparties/<party_id>', methods=['GET'])
def GetSpecificParty(party_id):
        partyid=None
        for party in PARTIES_DATA:
                app.logger.info(party)
                if party['id']==party_id:
                        partyid=party
                        app.logger.info(partyid.id)
                        break
                return partyid



@userbp.route('/getparty/<id>', methods=['PATCH'])
def GetSpecificPartyAndPatch(id):
    for party in PARTIES_DATA:
            if id==id:
                    
                    return jsonify (party)
                        
                       
@userbp.route('/deleteParty<id>',methods=['DELETE'])
def deleteParty(id):
        


       
        

    
     
        

