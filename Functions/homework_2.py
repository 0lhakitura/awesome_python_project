from collections import Counter
import unittest
import string


# TASK 1
def replace_character(expression):
    modified_string = ''
    for char in range(0, len(expression)):
        if expression[char] == '\"':
            modified_string += '\''
        elif expression[char] == '\'':
            modified_string += '\"'
        else:
            modified_string += expression[char]

    return modified_string


# TASK 2

def is_palindrome(expression):
    expression = expression.lower()
    expression = "".join(expression.split())
    for i in range(0, int(len(expression) / 2)):
        if expression[i] != expression[len(expression) - i - 1]:
            return 'No'
    return 'Yes'


# TASK 3

def get_shortest_word(expression):
    list_words = expression.split()
    list_words.sort(key=lambda a: len(a))
    return list_words[0]


# TASK 4

# characters that appear in all strings
def get_characters_in_all_strings(list_strings):
    result = set.intersection(*map(set, list_strings)) if list_strings else set()
    return sorted(result)


# characters that appear in at least one string
def get_characters_in_one_string(list_strings):
    result = set.union(*map(set, list_strings)) if list_strings else set()
    return sorted(result)


# characters that appear at least in two strings
def get_characters_in_two_string(list_strings):
    new_list = []
    for word in list_strings:
        for character in word:
            new_list.append(character)
    counter = Counter(new_list)
    characters_in_two_strings = []
    for y, x in counter.items():
        if x >= 2:
            characters_in_two_strings.append(y)
    return characters_in_two_strings


# characters of alphabet, that were not used in any string
def get_not_used_alphabet_characters(list_strings):
    new_list = []
    for word in list_strings:
        for character in word:
            new_list.append(character)
    alphabet = set(string.ascii_lowercase)
    set_not_used_alphabet_characters = alphabet.symmetric_difference(set(new_list))
    return sorted(set_not_used_alphabet_characters)


# TASK 5
# VARIATION 1
def count_letters_1(expression):
    all_freq = {}
    for i in expression:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq


# TASK 5
# VARIATION 2
def count_letters_2(expression):
    counter = Counter(expression)
    return counter


# TASK 5
# VARIATION 3
def count_letters_3(expression):
    counter = {}
    for character in expression:
        if character not in counter:
            counter[character] = 0
        counter[character] += 1
    return counter


class TestStringMethods(unittest.TestCase):

    def test_replace_character(self):
        expected = "Marine \"Banana\' \"Vasya\""
        actual = "Marine \'Banana\" \'Vasya\'"
        self.assertEqual(replace_character(actual), expected)

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('Never odd or even'), 'Yes')

    def test_get_shortest_word(self):
        self.assertEqual(get_shortest_word('Python is simple and effective!'), 'is')

    def tests_task_4(self):
        test_strings = ["hello", "world", "python", ]
        expected_characters_in_all_strings = ['o']
        expected_characters_in_one_string = ['d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y']
        expected_characters_in_two_string = ['h', 'l', 'o']
        expected_not_used_alphabet_characters = ['a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x',
                                                 'z']
        self.assertEqual(get_characters_in_all_strings(test_strings), expected_characters_in_all_strings)
        self.assertEqual(get_characters_in_one_string(test_strings), expected_characters_in_one_string)
        self.assertEqual(get_characters_in_two_string(test_strings), expected_characters_in_two_string)
        self.assertEqual(get_not_used_alphabet_characters(test_strings), expected_not_used_alphabet_characters)

    def tests_task_5(self):
        test_string = 'stringsample'
        dict_counted_letters = {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}
        self.assertEqual(count_letters_1(test_string), dict_counted_letters)
        self.assertEqual(count_letters_2(test_string), dict_counted_letters)
        self.assertEqual(count_letters_3(test_string), dict_counted_letters)


if __name__ == '__main__':
    unittest.main()