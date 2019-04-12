import unittest
from typing import List

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

input_values = [2, 7, 9, 3, 1]
output_value = 12


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.rob(input_values), output_value)


# can use temp vars to hold max values instead of save in array, array easier to trace path though
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) < 3:
            return max(nums)
        else:
            for i in range(2, len(nums)):
                if i < 3:
                    nums[i] += nums[i - 2]
                else:
                    nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
