arr = list(map(int,input().split()))
n = int(input())
a = []
for i in range(len(arr)):
    b = abs(arr[i] - n)
    a.append(b)
c= min(a)
s = a.index(c)
print(arr[s])