import unittest
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)
        if len_cost == 0:
            return 0
        elif len_cost < 3:
            return min(cost)
        else:
            for i in range(2, len_cost):
                cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])
            return min(cost[i - 1], cost[i])

        # O(1) storage
        # c1, c2 = 0, 0
        # for cost in reversed(cost):
        #     c1, c2 = cost + min(c1, c2), c1
        # return min(c1, c2)


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        expected = 6
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
