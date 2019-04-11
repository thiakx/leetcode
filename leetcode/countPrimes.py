import unittest


class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 3:
            return (0)
        else:

            prime_list = [True] * n
            prime_list[0] = False
            prime_list[1] = False

            for num in range(2, n):
                # if not yet blocked, all following divisible numbers are not prime
                if prime_list[num]:
                    # set all slots divisisble by number to false
                    prime_list[num::num] = [False] * len(prime_list[num::num])
                    prime_list[num] = True  # set the current prime number back to True

            return (sum(prime_list))


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.countPrimes(10)
        expected = 4
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
