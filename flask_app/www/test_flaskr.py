import unittest

import flaskr


class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = flaskr.app.test_client()
        self.db = flaskr.db
        self.migrate = flaskr.migrate
        with flaskr.app.app_context():
            self.db.create_all()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 200
        print(response)


if __name__ == '__main__':
    unittest.main(exit=False)
