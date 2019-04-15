import unittest
from typing import List


# You are given coins of different denominations and a total amount of money amount. Write a function to compute
# the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change_amount = [float('inf')] * (amount + 1)
        change_amount[0] = 0

        for i in range(1, len(change_amount)):
            for coin in coins:
                if coin > i:
                    pass
                else:
                    if coin == i:
                        change_amount[i] = 1
                    else:
                        change_amount[i] = min(1 + change_amount[i - coin], change_amount[i])

        optimal_change = change_amount[-1]

        if optimal_change == float('inf'):
            return -1
        else:
            return int(optimal_change)


class Test(unittest.TestCase):
    def test_three_change(self):
        solution = Solution()
        actual = solution.coinChange([1, 2, 5], 11)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
