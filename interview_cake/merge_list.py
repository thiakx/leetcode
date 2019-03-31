import unittest


def merge_lists(my_list, alices_list):
    # Combine the sorted lists into one large sorted list
    combined_list = []

    len_my_list = len(my_list)
    len_alices_list = len(alices_list)

    if len_my_list == 0 and len_alices_list == 0:
        return []
    elif len_my_list == 0:
        return alices_list
    elif len_alices_list == 0:
        return my_list

    my_pointer_pos = 0
    alice_pointer_pos = 0

    while my_pointer_pos <= len_my_list - 1 or alice_pointer_pos <= len_alices_list - 1:

        # mylist is exhausetd, just merge in alice list
        if my_pointer_pos > len_my_list - 1:
            combined_list.append(alices_list[alice_pointer_pos])
            alice_pointer_pos += 1
        elif alice_pointer_pos > len_alices_list - 1:
            # alice list is exhausetd, just merge in my_list
            combined_list.append(my_list[my_pointer_pos])
            my_pointer_pos += 1
        elif my_list[my_pointer_pos] <= alices_list[alice_pointer_pos]:
            combined_list.append(my_list[my_pointer_pos])
            my_pointer_pos += 1
        else:
            combined_list.append(alices_list[alice_pointer_pos])
            alice_pointer_pos += 1

    return combined_list


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)