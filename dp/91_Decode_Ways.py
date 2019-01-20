import unittest

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

s = "226"
output_value = 3


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numDecodings(s), output_value)


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == "":
            return 0
        # we don't care about the exact alphabets, we only care about number of ways
        # dp store number of ways for each char in s
        dp = [1] + n * [0]

        # by default, each non zero number has 1 way +
        # consider the 2 digits combo before current number.
        # (there are 27 letters, don't need consider beyond 2 digits combo)
        for i in range(1, n + 1):
            if s[i - 1] != "0":  # 0 has no matching alphabet
                dp[i] += dp[i - 1]
            if i != 1 and "09" < s[i - 2:i] < "27":
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
