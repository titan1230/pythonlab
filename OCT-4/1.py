# compare 3 nums are get the largest

def compare(x,y,z):
    l = [x,y,z]
    l.sort()

    return l[-1]

a = int(input("ENTER FIRST NUMBER: "))
b = int(input("ENTER SECOND NUMBER: "))
c = int(input("ENTER THIRD NUMBER: "))

print(f"\nTHE LARGEST NUMBER IS {compare(a,b,c)}")