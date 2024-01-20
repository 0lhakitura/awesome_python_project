import argparse

parser = argparse.ArgumentParser(description='Calculate result of simple mathematical operations')
parser.add_argument('integer1',
                    metavar='N1',
                    type=int,
                    help='an integer')

parser.add_argument('input',
                    help='input')

parser.add_argument('integer2',
                    metavar='N2',
                    type=int,
                    help='an integer')

args = parser.parse_args()

if args.input == '+':
    print(args.integer1 + args.integer2)

elif args.input == '-':
    print(args.integer1 - args.integer2)

elif args.input == '*':
    print(args.integer1 * args.integer2)

elif args.input == '/':
    print(args.integer1 / args.integer2)
else:
    raise NotImplementedError("Non-mathematical function")