"""def Operationchoice(c,a,b):
    if c == 1:
        return a+b
    elif c==2:
        return a-b
    elif c==3:
        return a*b
    elif c==4:
        return a/b
    else:
        return "invalid operator"
c = int(input())
a = int(input())
b = int(input()) 
print(Operationchoice(c,a,b))"""

c = int(input())
a = int(input())
b = int(input()) 
if c == 1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("invalid operator")

