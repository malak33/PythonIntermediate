"""

    Run as follows:

    05_argparse2.py -n John Smith -m

"""
import argparse
import pprint

parser = argparse.ArgumentParser(description='Personal characteristics')
parser.add_argument('-n', '--name', nargs='*', help='The name of the person', default='(no name)')
parser.add_argument('-a', '--age', help='The age of the person in years', default=0, type=int)
parser.add_argument('-m', '--isMale', help='Is the person a male', action='store_true')
args = parser.parse_args()
print(args)

pprint.pprint(args.__dict__, width=1, indent=2)