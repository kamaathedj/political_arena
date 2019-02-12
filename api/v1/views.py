from api.v1.models import createParty,CreateOffice,POLITICAL_OFFICE,PARTIES_DATA

from flask import Flask,jsonify,request,logging,Blueprint,make_response


app=Flask(__name__)

userbp=Blueprint("apiv1",__name__,url_prefix = "/api/v1")


party_data=createParty()
office_data=CreateOffice()

@userbp.route('/parties', methods=['POST'])
def create():
    data=request.get_json(force=True)
    # app.logger.info(data)
    
    id=len(PARTIES_DATA)+1
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
    message=""
    data=request.get_json()
    if data:
            id=len(POLITICAL_OFFICE)+1
            name=data['name']
            mtype=data['type']
    
    
   
            new_office={ "id":id, "name":name,"type":mtype}
            office_data.offices(new_office)
            message="Created"
            
            
           
    else:
            
            message="no data"
    
    

    return jsonify({"message":message},201)
    
    
@userbp.route('/offices', methods=['GET'])
def GetPoliticalOffices():
   resp=office_data.GetAllOffices()
   
   return jsonify({"message":resp})




@userbp.route('/offices/<int:office_id>',methods=['GET'])
def GetSpecificOffice(office_id):
        specific_office=office_data.GetOfficeId(office_id)
      
        mOffice=[]
         
        mOffice.append(specific_office)

        
        return jsonify({"message": mOffice})
     

        
       



            
                        
                        
         

       
        

    
     
        

