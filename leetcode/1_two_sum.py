import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_dict = {}

        for i, num in enumerate(nums):
            if num in num_dict:
                return [num_dict[num], i]
            else:
                num_dict[target - num] = i

        return [-1, -1]


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.twoSum([2, 7, 11, 15], 9)
        expected = [0, 1]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
