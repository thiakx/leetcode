import unittest


def change_possibilities(amount, denominations):
    # Calculate the number of ways to make change

    n_cents_amount = [0] * (amount + 1)
    n_cents_amount[0] = 1

    # the same coin only have 1 way of reaching the amount (combination, not permutation)
    # think about how many ways to reach X.
    # X = 2, we can do 1+1, or 2.
    # X = 4, we can do 1+1+2, 2+2 or 1+1+1+1
    for coin in denominations:
        for value in range(coin, amount + 1):
            n_cents_amount[value] += n_cents_amount[value - coin]
    return n_cents_amount[-1]


# Tests

class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = change_possibilities(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = change_possibilities(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = change_possibilities(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = change_possibilities(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = change_possibilities(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = change_possibilities(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)