import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack_set = set(haystack)
        needle_len = len(needle)
        haystack_len = len(haystack)

        if needle == '':
            return 0
        elif haystack == '' or haystack_len < needle_len:
            return -1
        else:
            if needle[0] not in haystack_set:
                return -1
            else:
                for i in range(haystack_len - needle_len + 1):
                    if haystack[i:i + needle_len] == needle:
                        return i
                    else:
                        pass
                return -1


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.strStr('hello', 'll')
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
