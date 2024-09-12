"""def calculate(n):
        ans = 0
        level =1
        while (level<=n):
            ans+=level*3
            level+=1
        ans-=n
        return ans
print(calculate(4))"""

"""n = int(input())
if n>0:
    print(n*(3*n+1)//2)
else:
    print(-1)"""
        
"""def calculate(n):
    if n<0:
        return -1
    else:
        return n*(3*n+1)//2
n = int(input())
print(calculate(n))"""

def fun(n):
    sum = 0
    if n==0:
        return -1
    for i in range(1,n+1):
        level=i*3
        sum = sum + level
    return sum-n
n = int(input())
print(fun(n))