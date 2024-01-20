from enum import Enum
import unittest


class SortOrder(Enum):
    ASC = 1
    DESC = 2


# Task 1

def find_value(integer):
    if integer > 0:
        return int(pow(integer, 2))
    elif integer < 0:
        return int(abs(integer))
    elif integer == 0:
        return 0


# Task 2

def sort_number_starting_from_maximum(integer):
    if type(integer) == int and 100 <= integer <= 999:
        v1 = int(integer / 100)
        v2 = int((integer / 10) % 10)
        v3 = (integer % 100) % 10
        minimum = min(min(v1, v2), v3)
        maximum = max(max(v1, v2), v3)
        v2 = (v1 + v2 + v3) - minimum - maximum
        integer = ((maximum * 100) + (v2 * 10) + minimum)
    else:
        raise ValueError("Wrong value!")
    return integer


# Task 3

def calculate_sum_of_odd_numbers(integer):
    if type(integer) == int and integer > 0:
        odd_digits_sum = 0
        while integer > 0:
            last_digit = int(integer % 10)
            if last_digit % 2 != 0:
                odd_digits_sum += last_digit
            integer = integer / 10
    else:
        raise ValueError("Wrong value!")
    return odd_digits_sum


# Task 4

def calculate_sum_of_binary_value(integer):
    string_of_binaries = bin(integer)
    list_of_binaries = list(string_of_binaries[2:])
    sum_of_binaries = 0
    if type(integer) == int and integer > 0:
        for binary_value in list_of_binaries:
            if binary_value == '1':
                sum_of_binaries = sum_of_binaries + 1
    else:
        raise ValueError("Wrong value!")
    return sum_of_binaries


# Task 5

def calculate_sum_of_first_n_fibonacci_numbers(n):
    f = [0, 1]
    if type(n) == int and n > 0:
        for i in range(2, n):
            f.insert(i, f[i - 1] + f[i - 2])
    else:
        raise ValueError("Wrong value!")
    return sum(f)


# Task 6

def is_array_sorted(sort_order, array):
    if len(array) == 0:
        raise ValueError("Wrong argument!")

    count = 0
    if sort_order == SortOrder.ASC:
        for i in range(0, len(array) - 1):
            if array[i] <= array[i + 1]:
                count = count + 1
    elif sort_order == SortOrder.DESC:
        for i in range(0, len(array) - 1):
            if array[i] >= array[i + 1]:
                count = count + 1

    return count == len(array) - 1


class TestMethods(unittest.TestCase):

    def test_find_value(self):
        self.assertEqual(find_value(4), 16)
        self.assertEqual(find_value(-5), 5)
        self.assertEqual(find_value(0), 0)

    def test_sort_number_starting_from_maximum(self):
        self.assertEqual(sort_number_starting_from_maximum(165), 651)
        self.assertEqual(sort_number_starting_from_maximum(879), 987)

    def test_calculate_sum_of_odd_numbers(self):
        self.assertEqual(calculate_sum_of_odd_numbers(1234), 4)
        self.assertEqual(calculate_sum_of_odd_numbers(246), 0)

    def test_calculate_sum_of_binary_value(self):
        self.assertEqual(calculate_sum_of_binary_value(14), 3)
        self.assertEqual(calculate_sum_of_binary_value(128), 1)

    def test_calculate_sum_of_first_n_fibonacci_numbers(self):
        self.assertEqual(calculate_sum_of_first_n_fibonacci_numbers(8), 33)
        self.assertEqual(calculate_sum_of_first_n_fibonacci_numbers(11), 143)

    def test_is_array_sorted(self):
        self.assertTrue(is_array_sorted(SortOrder.ASC, [51, 52, 53, 54]))
        self.assertTrue(is_array_sorted(SortOrder.DESC, [54, 53, 53, 51]))
        self.assertFalse(is_array_sorted(SortOrder.ASC, [51, 54, 53, 54]))
        self.assertFalse(is_array_sorted(SortOrder.DESC, [51, 53, 52, 51]))


if __name__ == '__main__':
    unittest.main()
