import unittest
from solution import has_consecutive_diff_one

class TestConsecutiveDifference(unittest.TestCase):

    def test_valid_increasing(self):
        self.assertTrue(has_consecutive_diff_one([1, 2, 3, 4]))

    def test_valid_decreasing(self):
        self.assertTrue(has_consecutive_diff_one([4, 3, 2, 1]))

    def test_mixed_valid(self):
        self.assertTrue(has_consecutive_diff_one([3, 4, 3, 4]))

    def test_invalid_case(self):
        self.assertFalse(has_consecutive_diff_one([1, 3, 4]))

    def test_single_element(self):
        self.assertTrue(has_consecutive_diff_one([10]))

    def test_two_elements_valid(self):
        self.assertTrue(has_consecutive_diff_one([5, 6]))

    def test_two_elements_invalid(self):
        self.assertFalse(has_consecutive_diff_one([5, 8]))


if __name__ == "__main__":
    unittest.main()
