import unittest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == 0 or len(points) == 0:
            return []
        else:
            points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
            return points[:K]


class Test(unittest.TestCase):
    def test_simple(self):
        solution = Solution()
        actual = solution.kClosest([[1, 3], [-2, 2]], 1)
        expected = [[-2, 2]]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
