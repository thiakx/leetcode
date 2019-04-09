import unittest

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

s = "leetcode"
wordDict = ["leet", "code"]
output_value = True


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.wordBreak(s, wordDict), output_value)


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = n * [False]
        for i in range(n):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (dp[i - len(w)] or i - len(w) == -1):
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
