"""def negative_growth(A,N):
    negative =0
    for i in range(1,N):
        if A[i] < A[i-1]:
            negative += 1
    return negative
N = int(input())
A = list(map(int,input().split()))
print(negative_growth(A,N))"""

n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(n):
    if a[i] < 0:
        count += 1
        result = count
    else:
        result = "not there"
    
print(result)