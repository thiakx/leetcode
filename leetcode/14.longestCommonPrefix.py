import unittest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        common_prefix = strs[0]
        # if blank, can return ''
        if common_prefix == '':
            return ''

        for i in range(1, len(strs)):

            # if blank, can return ''
            if strs[i] == '':
                return ''

            j = 0
            continue_loop = True

            # truncate common prefix to shorter word length
            if len(common_prefix) > len(strs[i]):
                common_prefix = common_prefix[:len(strs[i])]

                # common_prefix must be <= length than target after truncate
            while j < len(common_prefix) and continue_loop:
                if common_prefix[j] != strs[i][j]:
                    common_prefix = common_prefix[:j]  # exclude j which is not common
                    continue_loop = False
                j += 1

        if len(common_prefix) == 0:
            return ''
        else:
            return common_prefix


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.longestCommonPrefix(["flower", "flow", "flight"])
        expected = 'fl'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
