import base64
import unittest
from app import create_app

class TestFlaskApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def get_auth_header(self):
        username = 'dummy'
        password = 'dummy'
        auth_value = base64.b64encode(f"{username}:{password}".encode()).decode('utf-8')
        return {"Authorization": f"Basic {auth_value}"}

    def test_health(self):
        response = self.client.get('/api/v1/health', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)

    def test_version(self):
        response = self.client.get('/api/v1/version', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)

    def test_categories(self):
        response = self.client.get('/api/v1/categories', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)

    def test_get_coin(self):
        response = self.client.get('/api/v1/coins/bitcoin', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_coin(self):
        response = self.client.get('/api/v1/coins/invalid_coin', headers=self.get_auth_header())
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()