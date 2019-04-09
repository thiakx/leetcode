import unittest
import math

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

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # maintain two variables: min price max profit
        minprice = math.inf
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]  # buy
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice  # sell
        return maxprofit


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)  # extra conditions for jupyter notebook
