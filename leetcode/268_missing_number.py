import unittest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)  # use hashset to get constant time
        # reverse of usual comparison
        for num in range(len(nums) + 1):
            if num not in nums:
                return num


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.missingNumber([3, 0, 1])
        expected = 2
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
