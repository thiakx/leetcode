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
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_ways = [0, 1, 1]
        # dp, treat it as fibonacci sequence. 0,1,1,2,3,5,8 ....
        for i in range(3, n + 2):
            num_ways.append(num_ways[-1] + num_ways[-2])
        return num_ways[-1]


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
