import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sum_array = ''
        position_a = len(a) - 1
        position_b = len(b) - 1
        while position_a >= 0 and position_b >= 0:
            temp_sum = int(a[position_a]) + int(b[position_b]) + carry
            sum_array += str(temp_sum % 2)
            if temp_sum >= 2:
                carry = 1
            else:
                carry = 0
            position_a -= 1
            position_b -= 1

        if position_a >= 0:
            while position_a >= 0:
                temp_sum = int(a[position_a]) + carry
                sum_array += str(temp_sum % 2)
                if temp_sum >= 2:
                    carry = 1
                else:
                    carry = 0
                position_a -= 1
        else:
            while position_b >= 0:
                temp_sum = int(b[position_b]) + carry
                sum_array += str(temp_sum % 2)
                if temp_sum >= 2:
                    carry = 1
                else:
                    carry = 0
                position_b -= 1

        if carry > 0:
            sum_array += str(carry)

        return sum_array[::-1]


class Test(unittest.TestCase):

    def test_short(self):
        solution = Solution()
        result = solution.addBinary('1010', '1011')
        expected = '10101'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
