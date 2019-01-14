import unittest

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
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs_temp = costs
        if len(costs_temp) == 0:
            return 0
        elif len(costs_temp) == 1:
            return min(costs_temp[0])
        else:
            # keep first house values, start from 2nd house
            for i in range(1, len(costs_temp)):
                costs_temp[i][0] += min(costs_temp[i - 1][1], costs_temp[i - 1][2])  # cannot be red
                costs_temp[i][1] += min(costs_temp[i - 1][0], costs_temp[i - 1][2])  # cannot be green
                costs_temp[i][2] += min(costs_temp[i - 1][0], costs_temp[i - 1][1])  # cannot be blue
            return min(costs_temp[-1])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
