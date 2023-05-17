import unittest

class MultipleTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.X = 5
        cls.Y = 10

    def test_method1(self):
        Mul = self.X * self.Y
        if Mul == 50:
            print("Test Case 1 Passed")

    def test_method2(self):
        Sum = self.X + self.Y
        if Sum == 15:
            print("Test Case 2 Passed")

    def test_method3(self):
        division = self.Y // self.X
        if division == 2:
            print("Test Case 3 Passed")


if __name__ == '__main__':
    unittest.main()
