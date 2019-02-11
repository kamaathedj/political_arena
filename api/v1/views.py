from api.v1.models import createParty,CreateOffice
import random
from flask import Flask,jsonify,request,logging,Blueprint,make_response


app=Flask(__name__)

userbp=Blueprint("apiv1",__name__,url_prefix = "/api/v1")


party_data=createParty()
office_data=CreateOffice()

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
   
    party_data.parties(new_party)

    
    
    return make_response(jsonify({
            "status":201,
            "msg":"Created"
    }),201)

@userbp.route('/parties', methods=['GET'])
def GetParties():
        parties=party_data.Getparties()
       
        return jsonify({"message":parties})
    

@userbp.route('/party/<party_id>',methods=['GET'])
def GetSpecificParty(party_id):
       
        
        specific_party=party_data.getPartyId(party_id)
      
        mparty=[]
         
        mparty.append(specific_party)

        
        return jsonify({"message": mparty})
     
        
        


       


@userbp.route('/parties/<int:partyid>', methods=['PATCH'])
def SpecificPartyAndPatch(partyid):
        data=request.get_json()
        name=data['name']
        specific_party=party_data.GetSpecificPartyAndPatch(partyid,name)
        
      
        return jsonify({"message":"success"},200)
      

   
                        
                       
@userbp.route('/parties/<int:partyid>',methods=['DELETE'])
def deleteParty(partyid):
        message=party_data.GetSpecificPartyAndDelete(partyid)
        return jsonify({"message":message},200)


                
                       
        

               
      
@userbp.route('/offices', methods=['POST'])
def createOffice():
    data=request.get_json()
   
    
    id=random.randint(5,100)
    name=data['name']
    type=data['type']
    
   
    new_office={
            "id":id,
            "name":name,
            "type":type
            
    }
    office_data.offices(new_office)

    return jsonify({"message":"Created"},201)
    
    
@userbp.route('/offices', methods=['GET'])
def GetPoliticalOffices():
   resp=office_data.GetAllOffices()

   return jsonify({"Message":resp})



@userbp.route('/offices/<int:office_id>',methods=['GET'])
def GetSpecificOffice(office_id):
        specific_office=office_data.GetOfficeId(office_id)
      
        mOffice=[]
         
        mOffice.append(specific_office)

        
        return jsonify({"message": mOffice})
     

        
       



            
                        
                        
         

       
        

    
     
        

