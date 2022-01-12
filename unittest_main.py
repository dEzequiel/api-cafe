import unittest
from main import *

class APICafeTest(unittest.TestCase):
    
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        
        self.assertEqual(response.status_code, 200)
    
    def test_get_random_cafe(self):
        tester = app.test_client(self)
        response = tester.get('/random')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'id' in response.data)
    
    def test_get_all_cafe(self):
        tester = app.test_client(self)
        response = tester.get('/all')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'id' in response.data)

    def test_get_cafe_by_location(self):
        tester = app.test_client(self)
        response = tester.get('/search?location=Shoreditch')

        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.content_type, "application/json")
        self.assertTrue(b'id' in response.data)

if __name__ == '__main__':
    unittest.main()