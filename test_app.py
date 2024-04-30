import unittest
from app import app

class TestHealthEndpointStatusCode(unittest.TestCase):
    def test_health_endpoint(self):
        apiTest = app.test_client(self)
        resp = apiTest.get('/health', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, {'status':'OK'})