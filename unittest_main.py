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
        self.assertIsInstance(get_random_cafe(), dict)
    

if __name__ == '__main__':
    unittest.main()