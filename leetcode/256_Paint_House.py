import unittest
from typing import List

# There are a row of n houses, each house can be painted with one of the three colors:
# red, blue or green. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is
# the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

input_values = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
output_value = 10


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minCost(input_values), output_value)


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        len_cost = len(costs)
        if len_cost == 0:
            return 0
        elif len_cost == 1:
            return min(costs[0])
        else:
            for i in range(1, len_cost):
                costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])  # cannot be red
                costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])  # cannot be green
                costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])  # cannot be blue
        return min(costs[len_cost - 1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
