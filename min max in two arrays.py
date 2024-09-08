arr1 = list(map(int,input().split()))
l1 = len(arr1)
arr = list(map(int,input().split()))
l2 =len(arr)
k = int(input())
a=0
b=0
for i in range(l1):
    if(arr1[i]>k):
        a = a+1
        
for j in range(l2):
    if arr[j]<k:
        b = b+1
print(max(a,b))