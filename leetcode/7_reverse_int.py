import unittest


class Solution:
    def reverse(self, x: int) -> int:

        # if allowed to use built in function
        # x_reversed = int(str(abs(x))[::-1])

        x_temp = abs(x)
        x_reversed = 0
        for i in range(len(str(x_temp))):
            x_reversed = x_reversed * 10 + x_temp % 10
            x_temp //= 10  # integer divide (same as python2)

        if x > 0 and x_reversed < 2 ** 31 - 1:
            return x_reversed
        elif x < 0 and -x_reversed > -2 ** 31:
            return -x_reversed
        else:
            return 0


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.reverse(12345)
        expected = 54321
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
