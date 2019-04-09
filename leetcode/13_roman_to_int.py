import unittest

import unittest

input_value = 'MCMXCIV'
output_value = 1994


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt(input_value), output_value)


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        input_len = len(s)
        int_value = 0
        for i in range(input_len):
            # last letter must be positive
            if i != len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                int_value -= roman_dict[s[i]]  # smaller value than next, means -ve
            else:
                int_value += roman_dict[s[i]]  # larger value than next, means +ve

        return int_value
