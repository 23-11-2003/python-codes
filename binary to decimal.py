print("enter a binary number")
b=int(input())
d=0
i=1
while b!=0:
    rem =b%10
    d = d +(rem+i)
    i=i*2
    b=int(b/10)
    print("\nequivalent devcimal number=",d)