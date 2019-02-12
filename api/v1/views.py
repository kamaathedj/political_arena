import ast
from api.v1.models import createParty,CreateOffice,POLITICAL_OFFICE,PARTIES_DATA

from flask import Flask,jsonify,request,logging,Blueprint,make_response, json


app=Flask(__name__)

userbp=Blueprint("apiv1",__name__,url_prefix = "/api/v1")


party_data=createParty()
office_data=CreateOffice()

@userbp.route('/parties', methods=['POST'])
def create():
    data=request.get_json(force=True)
    # app.logger.info(data)
    response=request.get_json(force=True)
    data = json.dumps(response)
    dictData = ast.literal_eval(data)
    if dictData:
            id=len(POLITICAL_OFFICE)+1
            name=dictData["name"]
            hqAddress=dictData["hqAddress"]
            logoUrl=dictData["logoUrl"]
            
            if isinstance(name, str) and isinstance(hqAddress, str) and isinstance(logoUrl,str):
                    new_party={ "id":id, "name":name,"hqAddress":hqAddress,"logoUrl":logoUrl}
   
                    party_data.parties(new_party)
                    message="Created" 
                    return jsonify({"message":message},201) 
                    
            else:
                    return jsonify({"status":400,"message":"all the data must be type string"},400)
    else:
            return jsonify({  "status":400, "message":"No data found" },400)

                
        
             
                 
             
                
            
    
   

@userbp.route('/parties', methods=['GET'])
def GetParties():
        parties=party_data.Getparties()
       
        return jsonify({"message":parties})
    

@userbp.route('/party/<party_id>', methods=['GET'])
def GetSpecificParty(party_id):
        try:
                id=int(party_id)
        except:
                return jsonify({"status" : 404, "message": "not found"}) 

        specific_party=party_data.getPartyId(id)
        if specific_party is None:
                return jsonify({"status" : 404, "message": "not found"}) 
        else:
                mparty=[]

                mparty.append(specific_party)

                return jsonify({"status" : 200, "message": mparty})           



      
        
        
        


       


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

    response=request.get_json(force=True)
    data = json.dumps(response)
    dictData = ast.literal_eval(data)
    
    print(data)
    

    if data:
            id=len(POLITICAL_OFFICE)+1
           
            name=dictData["name"]
            mtype=dictData["type"]
            if isinstance(name, str) and isinstance(mtype, str):
                    print(type(name),type(mtype))
                    new_office={ "id":id, "name":name,"type":mtype}
                    office_data.offices(new_office)
                    message="Created" 
                    return jsonify({"message":message},201) 
                    
            else:
                    return jsonify({"status":400,"message":"all the data must be type string"},400)
                
        
             
                 
                    
                     
           
    else:
            return jsonify({  "status":400, "message":"No data found" },400)
    
    

   
    
    
@userbp.route('/offices', methods=['GET'])
def GetPoliticalOffices():
   resp=office_data.GetAllOffices()
   
   return jsonify({"message":resp})




@userbp.route('/offices/<office_id>',methods=['GET'])
def GetSpecificOffice(office_id):
        try:
                id=int(office_id)
              
        except:
                return jsonify({"status":404,"Message":"not found"})
        variable_types = (int,)
        print(variable_types,type(variable_types))
        if isinstance(id,variable_types):
                specific_office=office_data.GetOfficeId(id)
        
                mOffice=[]
                
                mOffice.append(specific_office)

                return jsonify({"message": mOffice})
        else:
                return jsonify({"status":404,"Message":"id must be of type int"},404)
     

#       
    
     
        

