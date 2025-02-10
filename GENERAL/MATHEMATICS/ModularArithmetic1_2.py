#!/bin/python3

#1
print (11 % 6)
print (8146798528947 % 17)

#2 
#Fermat's little theirem
#a^(n-1) = 1 mod n where m % a != 0

def myMod(n, p, m):
    if (p == m - 1 and m % n != 0):
            print("1")
    else:
        print(pow(n, p, m))


myMod(273246787654, 65536, 65537, False)
