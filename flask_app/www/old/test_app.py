import unittest
import page

class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = page.app.test_client()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()