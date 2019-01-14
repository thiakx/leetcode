import unittest

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

input_values = [-2, 0, 3, -5, 2, -1]
output_value = -1  # sumRange(2, 5) -> -1


class funcTest(unittest.TestCase):
    def test(self):
        obj = NumArray(input_values)
        self.assertEqual(obj.sumRange(2, 5), output_value)


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        num_len = len(nums)
        self.total = (num_len + 1) * [0]
        for i in range(num_len):
            # use dp to keep track of cumulative sum
            self.total[i + 1] = self.total[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.total[j + 1] - self.total[i]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
