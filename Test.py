import unittest
from AutomationTask import add

class TestAutomationTask(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
    def test_add_positive_negative(self):
        self.assertEqual(add(2, -3), -1)
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
    def test_add_float(self):
        self.assertEqual(add(2.5, 3.5), 6.0)
    def test_add_failure(self):
        self.assertNotEqual(add(1, 2), 4)  
    def test_add_non_numeric(self):
        with self.assertRaises(TypeError):
            add("Hello", 3)  

if __name__ == '__main__':
    unittest.main()
