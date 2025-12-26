import unittest
from sliding import max_elements_greater_than_x


class TestSlidingWindow(unittest.TestCase):

    def test_basic_case(self):
        arr = [1, 5, 2, 6, 7, 3]
        self.assertEqual(max_elements_greater_than_x(arr, 3, 4), 2)

    def test_all_elements(self):
        arr = [10, 11, 12, 13]
        self.assertEqual(max_elements_greater_than_x(arr, 2, 5), 2)

    def test_no_elements(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(max_elements_greater_than_x(arr, 2, 10), 0)

    def test_error_k_too_large(self):
        with self.assertRaises(ValueError):
            max_elements_greater_than_x([1, 2, 3], 5, 1)


if name == "__main__":
    unittest.main()
