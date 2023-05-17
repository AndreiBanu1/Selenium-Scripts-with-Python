import unittest

class CreateDependencyBetweenTestCases(unittest.TestCase):
    X = 5
    Y = 10

    @classmethod
    def setUpClass(cls):
        cls.X = 5
        cls.Y = 10

    def test_method1(self):
        self.assertEqual(15, 14)

    @unittest.depends_on(test_method1)
    def test_method2(self):
        Sum = self.X + self.Y
        if Sum == 15:
            print("Test Case 2 Passed")

    @unittest.depends_on(test_method2)
    def test_method3(self):
        division = self.Y // self.X
        if division == 2:
            print("Test Case 3 Passed")


if __name__ == '__main__':
    unittest.main()
