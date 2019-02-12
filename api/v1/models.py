PARTIES_DATA = [{
    'id': 1,
    'name': 'Jubilee',
    'hqAddress': 'nairobi',
    'logoUrl': 'www.google.com',
    }]

POLITICAL_OFFICE = [{'id': 1, 'name': 'meme', 'type': 'president'}]


class createParty:

    def parties(self, mlist):
        PARTIES_DATA.append(mlist)
        return PARTIES_DATA

    def getPartyId(self, id):
        party_loop = None
        for party in PARTIES_DATA:
            if party['id'] == id:
                party_loop = party
                break
        return party_loop

    def Getparties(self):
        return PARTIES_DATA

    def GetSpecificPartyAndPatch(self, party_id, name):
        for party in PARTIES_DATA:
            if party['id'] == party_id:
                party['name'] = name
                break
            return party

    def GetSpecificPartyAndDelete(self, partyid):
        message = None
        for party in PARTIES_DATA:
            if party['id'] == partyid:
                PARTIES_DATA.remove(party)
                message = 'success'
            else:
                message = 'not found'
        return message


class CreateOffice:

    def offices(self, mdict):
        POLITICAL_OFFICE.append(mdict)
        return POLITICAL_OFFICE

    def GetAllOffices(self):
        return POLITICAL_OFFICE

    def GetOfficeId(self, id):
        office_loop = None
        for office in POLITICAL_OFFICE:
            if office['id'] == id:
                office_loop = office
                break
        return office_loop



			