import unittest

# Palindromic Substrings

input_value = "aba"
output_value = 4


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.countSubstrings(input_value), output_value)


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        num_pand = 0
        for i in range(2 * n - 1):
            left = int(i / 2)
            right = left + i % 2
            # while true, center expansion search for more matches
            while left >= 0 and right < n and s[left] == s[right]:
                num_pand += 1
                left -= 1
                right += 1
                print(left, right)
        return num_pand


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
