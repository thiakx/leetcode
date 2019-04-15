import unittest
from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            raise IndexError('need at least 2 indices')

        # get the values before_index
        product_no_curr_index = [0] * len(nums)
        # first multiplication is just 1 so won't affect
        product_no_curr_index[0] = 1

        # Part 1
        # multiply numbers to the left of index, exclude index
        # example: nums = [1,2,3,4]
        #                 [1,1,2,6]
        for i in range(len(nums) - 1):
            product_no_curr_index[i + 1] = product_no_curr_index[i] * nums[i]

        # Part 2
        # multiply with values after index, exclude index and on part1 result
        product_temp = 1

        for i in range(len(nums) - 1, -1, -1):
            product_no_curr_index[i] *= product_temp
            product_temp *= nums[i]

        return product_no_curr_index


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.productExceptSelf([1, 2, 3])
        expected = [6, 3, 2]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
