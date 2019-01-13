import unittest

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

input_values = [2,7,9,3,1]
output_value = 12
class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.rob(input_values), output_value)


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)
        if num_len == 1:
            return nums[0]
        elif num_len == 2:
            return max(nums[0],nums[1])
        else:
            prevMax = 0
            currMax = 0
            for i in range(num_len):
                temp = currMax
                currMax = max(prevMax + nums[i], currMax)
                prevMax = temp
            return currMax


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # extra conditions for jupyter notebook