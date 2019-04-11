import unittest


class Solution:
    def isHappy(self, n: int) -> bool:
        loop_limit = 100  # stop once limit is hit
        loop_number = 1
        check_happy = True

        # optimize: if already processed, not need do it again
        looped_values = set()

        while check_happy:
            n = str(n)
            n_sum = 0
            for num in n:
                n_sum += int(num) ** 2

            # is happy number
            if n_sum == 1:
                return True

            # not happy number
            else:

                # check/save the seen number
                if n_sum in looped_values:
                    return False  # we looped back to values seen before, no chance
                else:
                    looped_values.add(n_sum)

                # check again if below loop limit
                loop_number += 1

                if loop_number > loop_limit:
                    check_happy = False
                else:
                    n = n_sum
        return False


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.isHappy(19)
        expected = True
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
