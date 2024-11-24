import unittest
from AutomationTask import addNumbers

class TestAutomationTask(unittest.TestCase):

    def test_addNumbers_positive_numbers(self):
        self.assertEqual(addNumbers(2, 3), 5)
    def test_addNumbers_negative_numbers(self):
        self.assertEqual(addNumbers(-2, -3), -5)
    def test_addNumbers_positive_negative(self):
        self.assertEqual(addNumbers(2, -3), -1)
    def test_addNumbers_zero(self):
        self.assertEqual(addNumbers(0, 5), 5)
        self.assertEqual(addNumbers(5, 0), 5)
    def test_addNumbers_float(self):
        self.assertEqual(addNumbers(2.5, 3.5), 6.0)
    def test_addNumbers_failure(self):
        self.assertNotEqual(addNumbers(1, 2), 4)  
    def test_addNumbers_non_numeric(self):
        with self.assertRaises(TypeError):
            addNumbers("Hello", 3)  

if __name__ == '__main__':
    unittest.main()
