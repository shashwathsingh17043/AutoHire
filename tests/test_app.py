import unittest
from app.main import app

class AutoHireTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_upload_empty(self):
        response = self.client.post('/', data={})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()