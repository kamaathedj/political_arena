import unittest
import json
from run import app
from api import creating_app

class test_politico(unittest.TestCase):
    def setUp(self):
        self.app=creating_app(enviroment="testing")
        self.client=self.app.test_client()
        self.data_party={"id":1,"name":"odm","hqAddress":"nairobi","logoUrl":"gfgfgf"}
        self.office={"name":"uhuru kenyatta","type":"president"}

    def post(self, path='/parties', data={}):
        if not data:
            data = self.data_party

        resp = self.client.post(path='api/v1/parties', data=json.dumps(self.data_party), content_type='application/json')
        return resp

    def post_office(self, path='/offices', data={}):
        if not data:
            data = self.office
        resp = self.client.post(path='api/v1/', data=json.dumps(self.data_party), content_type='application/json')
        return resp
        
    def test_getall_parties(self):
        resp=self.client.get(path='api/v1/parties',content_type='application/json')
        self.assertEqual(resp.status_code,200)
    def test_name_should_be_string(self):
        pass

    def test_getting_a_single_party(self):
        party = self.post()
        path = '/api/v1/party/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_party(self):
        path = '/api/v1/parties/1'
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_getall_political_offices(self):
        resp=self.client.get(path='api/v1/offices',content_type='application/json')
        self.assertEqual(resp.status_code,200)

    def test_specific_office(self):
        office = self.post_office()
        path = '/api/v1/offices/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_office(self):
        response=self.client.delete("api/v1/parties/0",content_type='application/json')
        self.assertNotIn(response.data,"office deleted succesfully") 

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()