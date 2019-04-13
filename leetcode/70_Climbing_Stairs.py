import unittest

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

input_values = 2
output_value = 2


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.climbStairs(input_values), output_value)


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        steps = [0] * (n + 1)
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        for i in range(3,n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
