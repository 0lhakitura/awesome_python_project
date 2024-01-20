import argparse

parser = argparse.ArgumentParser(description='Calculate result of simple mathematical operations')

parser.add_argument('input',
                    help='input')

parser.add_argument('integer1',
                    metavar='N1',
                    type=int,
                    help='an integer')

parser.add_argument('integer2',
                    metavar='N2',
                    type=int,
                    help='an integer')

args = parser.parse_args()

try:
    if args.input == 'add':
        print(args.integer1 + args.integer2)

    elif args.input == 'subtract':
        print(args.integer1 - args.integer2)

    elif args.input == 'multiply':
        print(args.integer1 * args.integer2)

    elif args.input == 'divide':
        print(args.integer1 / args.integer2)
    else:
        raise NotImplementedError
except Exception:
    print("Problem occurred")