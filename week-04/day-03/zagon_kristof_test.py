import unittest
from zagon_kristof_work import Apple

class  AppleTest(unittest.TestCase):
   
    def test_apple(self):
        my_apple = Apple()
        self.assertEqual(my_apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()