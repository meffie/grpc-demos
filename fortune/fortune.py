
import os
import random
import sys
import glob

class CookieFile:

    def __init__(self, filename):
        with open(filename) as f:
            text = f.read()
        sep = os.linesep + '%' + os.linesep
        self.cookies = [c for c in text.split(sep) if c]
        if len(self.cookies) == 0:
            raise ValueError('No cookies found in file {0}'.format(filename))
        self.last = len(self.cookies) - 1

    @classmethod
    def filenames(cls, path):
        for name in glob.glob(os.path.join(path, '*')):
            if not os.path.isfile(name):
                continue
            if '.' in os.path.basename(name):
                continue
            yield name

    def pick(self):
        return self.cookies[random.randint(0, self.last)]

def main():
    filename = sys.argv[1]
    cf = CookieFile(filename)
    print(cf.pick())

if __name__ == '__main__':
    sys.exit(main())
