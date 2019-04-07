import unittest


def highest_product_of_3(list_of_ints):
    # Calculate the highest product of three numbers
    if len(list_of_ints) < 3:
        raise ValueError('Less Than 3 items!')

    # populate based on first 2
    max_value = max(list_of_ints[0], list_of_ints[1])
    min_value = min(list_of_ints[0], list_of_ints[1])
    max2_value = list_of_ints[0] * list_of_ints[1]
    min2_value = list_of_ints[0] * list_of_ints[1]
    # populate based on first 3
    max3_value = max2_value * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        max3_value = max(max3_value, current * max2_value, current * min2_value)
        max2_value = max(max2_value, current * max_value, current * min_value)
        min2_value = min(min2_value, current * max_value, current * min_value)
        max_value = max(max_value, current)
        min_value = min(min_value, current)

    return max3_value


# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)