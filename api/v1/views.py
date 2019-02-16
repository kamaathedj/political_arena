import ast
from api.v1.models import createParty, CreateOffice, POLITICAL_OFFICE, \
    PARTIES_DATA
from flask import Flask, jsonify, request, logging, Blueprint, \
    make_response, json
app = Flask(__name__)
userbp = Blueprint('apiv1', __name__, url_prefix='/api/v1')
party_data = createParty()
office_data = CreateOffice()


@userbp.route('/parties', methods=['POST'])
def create():
    data = request.get_json(force=True)
    response = request.get_json(force=True)
    data = json.dumps(response)
    dictData = ast.literal_eval(data)
    if dictData and dictData['name'] is not "" and dictData['hqAddress'] is not "" and dictData['logoUrl'] is not "":
        id = len(POLITICAL_OFFICE) + 1
        name = dictData['name']
        hqAddress = dictData['hqAddress']
        logoUrl = dictData['logoUrl']
        if isinstance(name, str) and isinstance(hqAddress, str) \
            and isinstance(logoUrl, str):
            for party in PARTIES_DATA:
                if party["name"] != name and party['logoUrl'] !=logoUrl:
                    continue
                else:
                    return jsonify({'Error': "Cannot register a party with the same name and type","status": 409}),409  


            new_party = {'id': id,'name': name,'hqAddress': hqAddress,'logoUrl': logoUrl}
            party_data.parties(new_party)
            message = 'Created, The party was succesfully created'
            return jsonify({'message': message}), 201
        else:
            return jsonify({'status': 400,
                           'message': 'The data you entered in the fieds are of diffrent type than the requires'
                           }),400
    else:
        return jsonify({'status': 400, 'message': 'No data found,please provide all the fields .'}),400


@userbp.route('/parties', methods=['GET'])
def GetParties():
    parties = party_data.Getparties()
    if parties == None:
        return jsonify({"message":"The requested resource is empty","status":404}),404
        
    return jsonify({'message': parties,"status":200}),200   

@userbp.route('/party/<party_id>', methods=['GET'])
def GetSpecificParty(party_id):
    try:
        id = int(party_id)
    except:
        return jsonify({'status': 404, 'message': ' The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again'}),404
    specific_party = party_data.getPartyId(id)
    if specific_party is None:
        return jsonify({'status': 404, 'message': ' The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again'}),404
    else:
        mparty = []
        mparty.append(specific_party)
        return jsonify({'status': 200, 'message': mparty}),200


@userbp.route('/parties/<partyid>', methods=['PATCH'])
def SpecificPartyAndPatch(partyid):
    try:
        id=int(partyid)
    except:
        return jsonify({"error":'bad request',"status":400}),400
    data = request.get_json()
    
    
    if data:
        name = data['name']
        if isinstance(name,str):
            specific_party = party_data.GetSpecificPartyAndPatch(id, name)
            return jsonify({'message': specific_party,'status':200}),200
        else:
            return jsonify({'Error': "please insert correct fields",'status':400}),400   
        
    else:
        return jsonify({"error":"No field provided","status":400}),400
    
@userbp.route('/parties/<partyid>', methods=['DELETE'])
def deleteParty(partyid):
    try:
        id=int(partyid)
    except:
        return jsonify({"error":"bad request",'status':400}),400
    message = party_data.GetSpecificPartyAndDelete(id)
    return jsonify({'message': message,'status':200}),200
    


@userbp.route('/offices', methods=['POST'])
def createOffice():
    response = request.get_json(force=True)
    data = json.dumps(response)
    dictData = ast.literal_eval(data)
    if data and dictData['name'] is not "" and dictData['type'] is not "":
        id = len(POLITICAL_OFFICE) + 1
        name = dictData['name']
        mtype = dictData['type']
        if isinstance(name, str) and isinstance(mtype, str):
            for office in POLITICAL_OFFICE:
               if office["name"] != name and office['type'] !=mtype:
                    continue
               else:
                   return jsonify({'message': "Cannot register an office twice"}),400  
            new_office = {'id': id, 'name': name, 'type': mtype}
            office_data.offices(new_office)
            message = 'Created'
            return jsonify({'message': message}),201           
        else:
            return jsonify({'status': 400,
                           'message': 'All the data must be type string'
                           }),400
    else:
        return jsonify({'status': 400, 'message': 'No data found,please provide all the data required'}),400


@userbp.route('/offices', methods=['GET'])
def GetPoliticalOffices():
    if PARTIES_DATA ==None:
         return jsonify({'error': "No requested data found on the server","status":400}),400

    resp = office_data.GetAllOffices()
    return jsonify({'message': resp,'status':200}),200

       


@userbp.route('/offices/<office_id>', methods=['GET'])
def GetSpecificOffice(office_id):
    try:
        id = int(office_id)
    except:
        return jsonify({'status': 404, 'Message': 'id must be  a number'}),404
    variable_types = (int, )
    if isinstance(id, variable_types) and id:
        specific_office = office_data.GetOfficeId(id)
        mOffice = []
        mOffice.append(specific_office)
        return jsonify({'message': mOffice})
    else:
        return jsonify({'status': 404,
                       'error': 'the requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.'}),400

