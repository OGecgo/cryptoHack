
a = 12
b = 8

#Euclids Algorithm
def gcd(a, b):

    if (a == 0): #gcd(a, 0) = a
        print(a)
        return
    if (b == 0): #gcd(0, b) = b
        print(a)
        return
    if (a == b): #gcd(a, a) = a
        print(a)
        return
    
    
    if (b > a): #a be allway biger than b
        c = b
        b = a
        a = c

    r0 = a
    r1 = b    
    
    while True:
        r0 = r0 % r1
        
        if (r0 == 0):
            print(r1)
            return
    
        r1 = r1 % r0
        
        if(r1 == 0):
            print(r0)
            return


gcd(66528, 52920)


