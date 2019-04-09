import unittest

# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps.
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.

input_values = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
output_value = 6


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.minCostClimbingStairs(input_values), output_value)


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c1, c2 = 0, 0
        for cost in reversed(cost): # so we can have the cost ready from the end state
            c1, c2 = cost + min(c1, c2), c1
        return min(c1, c2)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
