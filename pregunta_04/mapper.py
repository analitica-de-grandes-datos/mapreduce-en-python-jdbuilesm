#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clr_spc(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x;

def purpose_amount(x):
    return clr_spc(x[0])  + "*" + clr_spc(x[2])

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('   ')
    print(purpose_amount(result))
