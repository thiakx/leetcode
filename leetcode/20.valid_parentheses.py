import unittest


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping_dict = {')': '(',
                        '}': '{',
                        ']': '['}

        if not s:
            return True
        else:
            for char in s:
                if char in mapping_dict:
                    if len(stack) == 0 or stack.pop() != mapping_dict[char]:
                        return False
                    else:
                        pass
                else:
                    stack.append(char)

        # should be empty stack by now if valid
        if len(stack) == 0:
            return True
        else:
            return False


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.isValid("([)]")
        expected = False
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
