import unittest
from logic import running_sum


class TestRunningSum(unittest.TestCase):

    def test_normal_case(self):
        data = [1, 2, 3]
        self.assertEqual(list(running_sum(data)), [1, 3, 6])

    def test_empty_list(self):
        data = []
        self.assertEqual(list(running_sum(data)), [])

    def test_negative_numbers(self):
        data = [5, -2, 4]
        self.assertEqual(list(running_sum(data)), [5, 3, 7])


if name == "__main__":
    unittest.main()import unittest
from logic import running_sum


class TestRunningSum(unittest.TestCase):

    def test_normal_case(self):
        data = [1, 2, 3]
        self.assertEqual(list(running_sum(data)), [1, 3, 6])

    def test_empty_list(self):
        data = []
        self.assertEqual(list(running_sum(data)), [])

    def test_negative_numbers(self):
        data = [5, -2, 4]
        self.assertEqual(list(running_sum(data)), [5, 3, 7])


if name == "__main__":
    unittest.main()
