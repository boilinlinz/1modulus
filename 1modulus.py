# This is an attempt to recreating the % modulo operator
# 
"""
 Find the remainder of a/b

 Find the largest number(c) (that is <b) that can be divided to a.
 if < 1, return a (a<b)
 if c == a, return a
 if a < b, remainder is a

ex. 5/3 = 1 rem.2
    25/5 = 5 rem.0
    25/26 0 rem.25
process outline:
a/b = c
1. Find highest number (g) that when multiplied to the divisor(b) is less than the dividend(a)
ex. 5/3 -> 3x1, 3x2, 3x3, 3x4..., -> g = 3x1 because 3x2 is > 5
2. Subtract the number (g) to the dividend(a) to get the remainder |   5 - g -> 5 - (3x1) -> 5-3 -> remainder = 2
3. if the divisor(b) can be multiplied to be equal the dividend(a), then the remainder is zero 
"""
def makeMod(a=0, b=0):
    try:
        a = abs(int(a))
        b = abs(int(b))
        g = 1
        for x in range(a+1):
            h = b * x 
            if h < a:   # Finds the highest number that when * to b is less than a
                g = h
                c = a - g   #Subtract highest number to the dividend
            elif h == a:   #If b can be multiplied to be equal to a, remainder is 0 
                c = 0
        return c
    except: 
        return None

a = input("Dividend: ")
b = input("Divsor: ")
c = makeMod(a,b)
#print("remainder of {}/{} is {}".format(a,b,c))
print(f"The remainder of {a}/{b} is {c}")
