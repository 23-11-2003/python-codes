"""def max(a,b):
    return a if a>b else b
l1,l2,r1,r2 = map(int,input().split())
max_product = max(max(max(l1*l2,l1*r2),max(r1*l2,r1*r2)),max(l1*r2,l2*r2))
print(max_product)"""

l1,l2,r1,r2 = map(int,input().split())
result = []
for i in range(l1,r1+1):
    for j in range(l2,r2+1):
        result.append(i*j)
print(max(result))