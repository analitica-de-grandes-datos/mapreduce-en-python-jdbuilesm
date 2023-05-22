#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clr_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def amount(x):
    return clr_spaces(x[1].split("-")[1])

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(amount(result))
