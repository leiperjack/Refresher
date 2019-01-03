import unittest
from multiplication import multiplication

class myClass(unittest.TestCase):
    def test_multipication(self):
        self.assertEqual(multiplication(6,3), (18))

if __name__ == "__main__":
    unittest.main()