#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
biggest = {}

def set_bigger_purpose(dict_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")
    dict_purposes[actual_element] = int(dict_purposes.get(actual_element) or 0) + 1 
    return dict_purposes

for line in sys.stdin:
    set_bigger_purpose(biggest, line)

for purpose, amount in biggest.items():
    print(purpose + "	" + str(amount))
