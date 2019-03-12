import unittest
import json
from run import app
from api import creating_app

class test_politico(unittest.TestCase):
    def setUp(self):
        self.app=app
        app.testing=True
        self.client=self.app.test_client()
        self.data_party={"id":1,"name":"odm","hqAddress":"nairobi","logoUrl":"gfgfgf"}
        self.data_party1={}
        self.office={"name":"uhuru kenyatta","type":"president"}
        self.office_empty={}

    def test_post(self):
        resp = self.client.post(path='api/v1/parties', data=json.dumps(self.data_party), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
    def test_empty(self):
        resp=self.client.post(path='api/v1/parties', data=json.dumps(self.data_party1), content_type='application/json')
        self.assertEqual(resp.status_code,400)

    def post_office(self, path='/offices', data={}):
        if not data:
            data = self.office
        resp = self.client.post(path='api/v1/', data=json.dumps(self.data_party), content_type='application/json')
        return resp
    # def test_empty_office(self):
    #     response=self.client.post("api/v1/offices",data=json.dumps(self.office_empty),content_type='application/json')
    #     self.assertEqual(response.status_code,400)
        
    def test_getall_parties(self):
        resp=self.client.get(path='api/v1/parties',content_type='application/json')
        self.assertEqual(resp.status_code,200)
    def test_name_should_be_string(self):
        pass

    def test_getting_a_single_party(self):
        response = self.client.get(path='api/v1/parties', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_party(self):
        path = '/api/v1/parties/1'
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_getall_political_offices(self):
        resp=self.client.get(path='api/v1/offices',content_type='application/json')
        self.assertEqual(resp.status_code,200)

    def test_specific_office(self):
        path = '/api/v1/offices/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_office(self):
        response=self.client.delete("api/v1/parties/0",content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_partyid_is_int(self):
        resp=self.client.get(path='api/v1/party/y',content_type='application/json')
        self.assertEqual(resp.status_code,404)
    def test_get_party_no_id(self):
        resp=self.client.get(path='api/v1/party/',content_type='application/json')
        self.assertEqual(resp.status_code,404)

    def test_get_office_not_int(self):
        resp=self.client.get(path='api/v1/offices/y',content_type='application/json')
        self.assertEqual(resp.status_code,404)

    def test_officeid_is_int(self):
        resp=self.client.get(path='api/v1/offices/1',content_type='application/json')
        self.assertEqual(resp.status_code,200)
    def test_get_office_no_id(self):
        resp=self.client.get(path='api/v1/offices/',content_type='application/json')
        self.assertEqual(resp.status_code,404)

    

    

    def tearDown(self):
        self.app.testing=False

if __name__ == "__main__":
    unittest.main()