import unittest


def has_palindrome_permutation(the_string):
    # Check if any permutation of the input is a palindrome
    # pali perm means all entries must be even with at most 1 entry with odd.

    p_dict = {}

    for char in the_string:
        if not char in p_dict:
            p_dict[char] = 1
        else:
            p_dict[char] += 1

    odd_flag = 0
    for v in p_dict.values():
        if v % 2 != 0:
            odd_flag += 1
        if odd_flag > 1:
            return False
    return True


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
