import unittest
import json
from run import app

party_data={}

class test_politico(unittest.TestCase):
    def setUp(self):
        self.app=app
        self.client=self.app.test_client()
        self.data_party={"id":1,"name":"odm","hqAddress":"nairobi","logoUrl":"gfgfgf"}

    def post(self, path='/parties', data={}):
        if not data:
            data = self.data_party

        resp = self.client.post(path='api/v1/parties', data=json.dumps(self.data_party), content_type='application/json')
        
        return resp

    def test_posting_a_political_party(self):
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
   
        # self.assertIsInstance(resp.json['name'],str)
        # self.assertTrue(resp.json["id"])
        self.assertEqual(resp.json['msg'], 'Created')

    def test_getall_parties(self):
        resp=self.client.get(path='api/v1/getparties',content_type='application/json')
        self.assertEqual(resp.status_code,200)
    def test_name_should_be_string(self):
        pass

    def test_getting_a_single_party(self):
        party = self.post()
        path = '/api/v1/specificparties/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_party(self):
        path = '/api/v1/deleteParty/1'
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        




    def test_getall_political_offices(self):
        resp=self.client.get(path='api/v1/getoffices',content_type='application/json')
        self.assertEqual(resp.status_code,200)

    def test_specific_office(self):
        office = self.post()
        path = '/api/v1/specificoffice/0'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


    
        


    

if __name__ == "__main__":
    unittest.main()