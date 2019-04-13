import unittest

# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

n = 3
k = 2
output_value = 6


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.numWays(3, 2), output_value)


class Solution:
    # reference: forums
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        else:
            same, diff = k, k * (k - 1)
            for i in range(3, n + 1):
                same, diff = diff, (same + diff) * (k - 1)
            return same + diff


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
