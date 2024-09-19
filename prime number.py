"""n = int(input())
#for num in range(2, n + 1):
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print("not Prime")
        break
    else:
        print("prime")"""

"""n = int(input())
count = 0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")"""
    
n = int(input())     #for print a prime numbers in a range
for i in range(1,n+1):
    if i>1:
        for j in range(2,i):
            if i%j== 0:
             break
        else:
            print(i)