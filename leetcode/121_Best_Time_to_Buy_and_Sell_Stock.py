import unittest
import math
from typing import List

# 121. Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
input_values = [7, 1, 5, 3, 6, 4]
output_value = 5


class funcTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(solution.maxProfit(input_values), output_value)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0
        # assume cannot -ve profit
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            # assume cannot buy and sell on same day
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)

        return max_profit


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
