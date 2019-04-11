import unittest


class Solution:
    def countAndSay(self, n: int) -> str:
        count_say_seq = '1'

        for _ in range(n - 1):
            prev = count_say_seq
            count_say_seq = ''
            j = 0
            while j < len(prev):
                curr = prev[j]
                count = 1
                j += 1
                while j < len(prev) and prev[j] == curr:
                    count += 1
                    j += 1
                count_say_seq += str(count) + str(curr)
        return count_say_seq


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.countAndSay(5)
        expected = '111221'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
