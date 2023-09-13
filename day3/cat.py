import fileinput
import sys

for line in fileinput.input():
    sys.stdout.write(line)

filename, ext = '...'.split('.', 1)
filename, _, ext = '...'.partition('.')