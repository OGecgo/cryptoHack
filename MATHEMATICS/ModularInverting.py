#!/bin/python3

#g^n-1 = 1 mod n
#g * g^n-2 = 1 mod n
# that mean g^n-2 is inverst number
def inversModul(g, n):
    print(pow(g, n - 2, n))
    
inversModul(3, 13)