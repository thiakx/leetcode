import unittest
from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fb_array = [''] * n
        fb_dict = {3: 'Fizz', 5: 'Buzz'}

        for i in range(n):
            actual_value = i + 1

            if actual_value % 3 == 0:
                fb_array[i] += fb_dict[3]
            if actual_value % 5 == 0:
                fb_array[i] += fb_dict[5]
            if fb_array[i] == '':
                fb_array[i] += str(actual_value)

        return fb_array


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.fizzBuzz(5)
        expected = ['1', '2', 'Fizz', '4', 'Buzz']
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
