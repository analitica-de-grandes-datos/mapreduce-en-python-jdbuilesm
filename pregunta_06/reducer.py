#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
biggest = {}
smaller = {}

def set_bigger_smaller(biggest, smaller, actual_element):
    element_array = actual_element.split("*")
    biggest[element_array[0]] = max(
        float(biggest.get(element_array[0]) or 0), float(element_array[1]))
    smaller[element_array[0]] = min(
        float(smaller.get(element_array[0]) or 10000), float(element_array[1]))
    return biggest, smaller

for line in sys.stdin:
    set_bigger_smaller(biggest, smaller, line)

for max, min in zip(biggest.items(), smaller.items()):
    print( max[0] + "	" + str(max[1]) + "	" + str(min[1]) )
