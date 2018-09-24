import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-k', '--key', required=True)
   # parser.add_argument('-n', '--name', '--val')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

   key=str(namespace.name)



