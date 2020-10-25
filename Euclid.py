# EUCLID'S ALGORITHM

def gcd(a,b):
    print()
    if a > b:
        a, b = b, a
    c = 1
    while c != 0:
        i,c = 0,1
        while ((i*a)+a)<=b:
            i = i+1
        c = b - (i*a)
        print(str(b)+" = "+str(a)+" x "+str(i)+" + "+str(c))
        print()
        b = a
        a = c
    print("GCD is " + str(b))
    print()
    
gcd(int(input("a: ")),int(input("\nb: ")))
