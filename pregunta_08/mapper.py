#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clr_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def purpose(x):
    return   clr_spaces(x[0])  + "*" + clr_spaces(x[2])

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(purpose(result))
