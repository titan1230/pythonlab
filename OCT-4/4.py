# accept a list from the user and check if elemets are list are even or odd

def check(a):

    l = []

    for i in a:
        if i%2==0:
            l.append(i)
    
    if len(l) == 0: return "NONE"
    else: return l


a = int(input("ENTER THE SIZE OF LIST TO CHECK: "))
li = []

while a>0:
    inp = int(input("ENTER NUMBER TO PUT IN LIST AND CHECK: "))
    li.append(inp)

    a -= 1

print(check(li))