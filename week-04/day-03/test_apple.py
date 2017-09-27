import unittest
from apple import Apple

class  AppleTest(unittest.TestCase):
   
    def test_apple(self):
        my_apple = Apple()
        self.assertEqual(my_apple.get_apple(), "apple")

if __name__ == '__main__':
    unittest.main()




# class AppleTest(unittest.TestCase):
#     def apple_test(self):
#         self.assertEqual(1, 1)

# if __name__ == "__main__":
#     unittest.main()
