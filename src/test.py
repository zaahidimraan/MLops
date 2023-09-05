import unittest
from main import addFunction, subFunction, mulFunction, divFunction


class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addFunction(1.0, 2.0), 3.0)

    def test_sub(self):
        self.assertEqual(subFunction(1.0, 2.0), -1.0)

    def test_mul(self):
        self.assertEqual(mulFunction(1.0, 2.0), 2)

    def test_div(self):
        self.assertEqual(divFunction(1.0, 2.0), 0.5)
        with self.assertRaises(ValueError):
            divFunction(1, 0)


if __name__ == '__main__':
    unittest.main()
