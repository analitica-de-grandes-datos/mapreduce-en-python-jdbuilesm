#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
big = {}

def set_big(dict, actual):
    element_array = actual.split("*")
    dict[element_array[0]] = int(dict.get(actual[0]) or 0) + 1 
    return dict

for line in sys.stdin:
    set_big(big, line)

for purpose, amount in big.items():
    print(purpose + "," + str(amount))
