import unittest


# reference: leetcode forums
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor > 0:
            if xor & 1:
                count += 1
            # >>: bit shift right
            xor = xor >> 1
        return count


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.hammingDistance(1, 4)
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
