import unittest
from typing import List


class Test(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()
        expected = ['o', 'l', 'l', 'e', 'h']
        actual = solution.reverse_string(['h', 'e', 'l', 'l', 'o'])
        self.assertListEqual(expected, actual)


class Solution(object):
    def reverse_string(self, s: List[str]) -> List[str]:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s

        # python way
        # s[:] = s[::-1]

        # iterative way, but wont be modifying in place.
        # l = len(s)
        # if l < 2:
        #     return s
        # self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
