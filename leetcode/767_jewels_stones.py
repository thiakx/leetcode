import unittest


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_set = set(J)
        gem_count = 0
        for stone in S:
            if stone in jewel_set:
                gem_count += 1
        return gem_count


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.numJewelsInStones("aA", "aAAbbbb")
        expected = 3
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
