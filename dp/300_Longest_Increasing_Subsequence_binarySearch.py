import unittest
import math
# Longest Increasing Subsequence

input_value = [10, 9, 2, 5, 3, 7, 101, 18]
output_value = 4


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.lengthOfLIS(input_value), output_value)


# with binary seach, reduce time complexity to O(nlog(n))
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

        dp = n * [0]
        temp_max = 0
        for x in nums:
            i = 0
            j = temp_max
            while i != j:
                m = math.floor((i + j) / 2)
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            temp_max = max(i + 1, temp_max)

        return temp_max


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
