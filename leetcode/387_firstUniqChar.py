import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:

        if len(s) == 0:
            return -1

        # count the chars first
        char_dict = {}
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        # loop again to find min
        for i in range(len(s)):
            if char_dict[s[i]] == 1:
                return i
            else:
                pass

        return -1


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.firstUniqChar("leetcode")
        expected = 0
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
