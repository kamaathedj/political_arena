from api.v1.models import createParty

from flask import Flask,jsonify,request,logging,Blueprint


userbp=Blueprint("apiv1",__name__,url_prefix = "/api/v1")


# app.logger.info('kamaa')
PARTY=[]
@userbp.route('/parties', methods=['POST'])
def create():
    data=request.get_json(force=True)
    # app.logger.info(data)
  
    name=data['name']
    hqAddress=data['hqAddress']
    logoUrl=data['logoUrl']
    # PARTY.append[data]
    new_party=createParty(name,hqAddress,logoUrl)
    PARTY.append(data)


   
    return jsonify(PARTY)