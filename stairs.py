import sys
import argparse

# Доделать
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--reversed', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))

steps = sys.argv[1]
# direction = sys.argv[2]

for i in range(0, int(steps)):
	print(" "*(int(steps)-i-1)+"#"*(i+1))