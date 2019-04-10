import unittest
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # find max from the end

        # edge cases
        # num1 empty, return num2
        if m == 0:
            nums1[:] = nums2[:]  # python trick to copy
        # num2 empty, do nothing, return num1
        elif n == 0:
            pass
        else:
            pointer1 = m - 1
            pointer2 = n - 1
            pointer1_end = m + n - 1

            while pointer1 >= 0 and pointer2 >= 0:
                nums1_temp = nums1[pointer1]
                nums2_temp = nums2[pointer2]

                if nums1_temp > nums2_temp:
                    nums1[pointer1_end] = nums1_temp
                    nums1[pointer1] = 0
                    pointer1 -= 1
                else:
                    nums1[pointer1_end] = nums2_temp
                    nums2[pointer2] = 0
                    pointer2 -= 1
                pointer1_end -= 1

            # if there are still left overs from num2, we fill forward. if num1, we do nothing, done.
            nums1[0:pointer2 + 1] = nums2[0:pointer2 + 1]

        return nums1


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.merge([0], 0, [1], 1)
        expected = [1]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
