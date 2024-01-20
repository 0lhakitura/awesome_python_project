import argparse
import numexpr

parser = argparse.ArgumentParser(description='Determine whether the input string is the correct entry '
                                             'for the formula according EBNF syntax ')
parser.add_argument('input', type=str)
args = parser.parse_args()

value = getattr(args, 'input')

sign_plus_minus = ['+', '-']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(len(value)):
    if value[i] in sign_plus_minus and value[i + 1] in sign_plus_minus:
        print(False, None)
    elif value[i] not in sign_plus_minus and value[i] not in numbers:
        print(False, None)
print(True, numexpr.evaluate(value))
