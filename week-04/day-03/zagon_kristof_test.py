import unittest
from zagon_kristof_work import Apple, Sum_of_the_Elements

class AppleTest(unittest.TestCase):
   
    def test_apple(self):
        my_apple = Apple()
        self.assertEqual(my_apple.get_apple(), "apple")



class Sum_of_the_ElementsTest(unittest.TestCase):
    
    def test_sum_of_numbers1(self):
        my_number = Sum_of_the_Elements()
        numlist = [0]
        self.assertEqual(my_number.sum_of_numbers(numlist),0)
        numlist = []
        self.assertEqual(my_number.sum_of_numbers(numlist),0)
        numlist = [1, 2, 3, 4]
        self.assertEqual(my_number.sum_of_numbers(numlist),10)
        numlist = None
        self.assertEqual(my_number.sum_of_numbers(numlist),None)
        

if __name__ == '__main__':
    unittest.main()


