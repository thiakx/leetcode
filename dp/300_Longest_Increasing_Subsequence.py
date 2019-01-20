import unittest

# Longest Increasing Subsequence

input_value = [10, 9, 2, 5, 3, 7, 101, 18]
output_value = 4


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(input_value), output_value)


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we only care about the length, not the actual combination
        n = len(nums)
        if n == 0:
            return 0

        dp = n * [1]
        for i in range(1, n):
            temp_max = 0
            # loop through the values before current i
            # review logic at: https://leetcode.com/articles/longest-increasing-subsequence/
            for j in range(0, i):
                if nums[i] > nums[j] and dp[j] > temp_max:
                    temp_max = dp[j]
                dp[i] = temp_max + 1

        return max(dp)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
