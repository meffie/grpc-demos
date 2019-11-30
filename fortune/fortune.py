
import os
import random
import sys


class CookieFile:

    def __init__(self, filename):
        with open(filename) as f:
            text = f.read().rstrip()
        record_sep = os.linesep + '%' + os.linesep
        self.cookies = text.split(record_sep)
        if len(self.cookies) == 0:
            raise ValueError('No cookies found in file {0}'.format(filename))
        self.last = len(self.cookies) - 1

    def pick(self):
        return self.cookies[random.randint(0, self.last)]

def main():
    filename = sys.argv[1]
    cf = CookieFile(filename)
    print(cf.pick())

if __name__ == '__main__':
    sys.exit(main())
