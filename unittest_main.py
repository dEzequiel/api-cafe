import unittest
from main import *

class APICafeTest(unittest.TestCase):

    def test_get_random_cafe(self):
        value = get_random_cafe()
        self.assertIsInstance(get_random_cafe(), dict)
