# -*- coding: utf-8 -*
import math
def get_p(s):

    l=len(s)
    if (l%2) == 0:
        return (s[int (l/2-1):int (l/2+1)])

    else:
        return (s[int (l/2)])

print(get_p('middle'))
print(get_p('A'))
print(get_p('testing'))
