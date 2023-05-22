#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def amount(x):
    return x[2]

for line in sys.stdin:
    result = line.split(',')
    print(amount(result))
