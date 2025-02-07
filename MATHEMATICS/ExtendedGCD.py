#!/bin/python3 

#Euclids Algorithm
def egcd(a, b):

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
        a, b = b, a
        
        
    x0, x1 = 0, 1
    y0, y1 = 1, 0  
    
    r0, r1 = a * y0, b * x0
    
    while True:
        print("{}=({} - {} * {})".format((x0 - x1 * (r0//r1)), x0, x1, r0//r1))
        
        q = r0//r1
        x0 = (x0 - x1 * q)
        y0 = (y0 - y1 * q)
        r0 = r0 % r1
        
        x0, x1, y0, y1 = x1, x0, y1, y0    
        r0, r1 = r1, r0
        
        if (r1 == 0):
            print(r0, x0, y0)
            return
    

        
        

a = 26513
b = 32321

egcd(a, b)


