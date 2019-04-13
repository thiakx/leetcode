import unittest
from typing import List, Union

# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

input_values = [-2, 0, 3, -5, 2, -1]
output_value = -1  # sumRange(2, 5) -> -1


class funcTest(unittest.TestCase):
    def test(self):
        obj = NumArray(input_values)
        self.assertEqual(obj.sumRange(2, 5), output_value)


class NumArray:

    def __init__(self, nums: List[int]):
        self.len_nums = len(nums)
        self.cumulative_sum = [0] * self.len_nums
        self.cumulative_sum[0] = nums[0]
        for i in range(1, self.len_nums):
            self.cumulative_sum[i] = nums[i] + self.cumulative_sum[i - 1]

    def sumRange(self, i: int, j: int) -> Union[int, None]:
        if self.len_nums == 0:
            return None
        elif i == 0:
            return self.cumulative_sum[j]
        else:
            return self.cumulative_sum[j] - self.cumulative_sum[i - 1]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
