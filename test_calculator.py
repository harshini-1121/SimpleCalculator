import unittest
from main import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 3), 6)

if __name__ == "__main__":
    unittest.main()
