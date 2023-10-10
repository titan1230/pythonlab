# prime or not

def checkPrime(a):
    if a<=1:
        return False
    elif a==2:
        return True
    else:

        for i in range(2, a):
            if a%1==0: return False
        else: return True

inp = int(input("ENTER NUMBER: "))

if checkPrime(inp):
    print("THE NUMBER IS PRIME")
else:
    print("THE NUMBER IS NOT PRIME")