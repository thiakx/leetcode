import unittest

# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
input_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output_value = 6


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxSubArray(input_values), output_value)


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray_values = [nums[0]]
        for i in range(1, len(nums)):
            if max_subarray_values[-1] < 0:
                max_subarray_values.append(nums[i])  # if negative, don't append previous value
            else:
                max_subarray_values.append(nums[i] + max_subarray_values[-1])
        return max(max_subarray_values)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
