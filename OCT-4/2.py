# check if +ve or -ve

def check(a):
    if a==0:
        return "NEITHER +VE OR -VE"
    elif a>0:
        return "-VE"
    else:
        return "+VE"

a = int(input("ENTER NUMBER: "))
print(f"THE NUMBER IS {check(a)}")