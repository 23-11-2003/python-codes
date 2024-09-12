"""def numerological(n):
    while n>9:
        sum = 0
        while n>0:
            sum += n%10
            n//=10
        n = sum
    return n
n = int(input())
print(numerological(n))"""

"""def numerological(n):
    if n==0:
        return 0
    if n%9==0:
        return 9
    else:
        print(n%9)
        
n = int(input())
numerological(n)"""

n = int(input())  #without def

if n == 0:
    result = 0
elif n % 9 == 0:
    result = 9
else:
    result = n % 9

print(result)
   