#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def clr_spaces(x):
    x = x.replace("\n", "")
    x = x.replace("\r", "")
    return x

def purpose(x):
    return  clr_spaces(x[0]), clr_spaces(x[1]).split(",")

for line in sys.stdin:
    line = line.replace("'","")
    result = line.split('\t')
    number, array = purpose(result) 
    for letter_array in array:
        print(letter_array + "*" + number)
