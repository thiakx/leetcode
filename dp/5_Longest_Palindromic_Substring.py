import unittest

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

input_value = "babad"
output_value = "aba"


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.longestPalindrome(input_value), output_value)


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: string
        :rtype: string
        """
        temp_str = ''
        n = len(s)
        dp = [[0] * n for i in range(n)]
        max_length = 0

        # compare reversed with front
        for i in reversed(range(n)):
            for j in range(i, n):
                # note that palindrome if only have 1 or two char is trivial, so start at 3
                # single row array, i + 1, j -1 to come back to center for compare
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if temp_str == '' or max_length < j - i + 1:
                        temp_str = s[i:j + 1]
                        max_length = j - i + 1
        return temp_str


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
