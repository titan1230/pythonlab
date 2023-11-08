# check int or not

def check(a):
    try:
        e = int(a)

        return "NUMBER IS INT"
    except ValueError:
        return "NUMBER IS NOT INT"

a = input("ENTER YOUR INPUT: ")