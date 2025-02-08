#!/bin/python3

#1
print (11 % 6)
print (8146798528947 % 17)

#2
#a^n+d mod n
#n prime and n+d not prime. that means a is allways even number because every prime without 2 is not even number

def myMod(n, p, m, modIsPrime = False):
    if modIsPrime:
        if (p % 2 == 0):
            print("mod is prime and p is even: 1")
        else:
            print(pow(n, p) % m)


myMod(273246787654, 65536, 65537, True)