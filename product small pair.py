"""def Productsmallpair(sum, arr):
    if len(arr) < 2 or sum < 2:
        return -1

    arr.sort()
    smallest = float('inf')
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                product = arr[i] * arr[j]
                if product < smallest:
                    smallest = product

    return smallest if smallest != float('inf') else 0
sum = int(input())
arr = list(map(int,input().split()))
print(Productsmallpair(sum, arr))"""

sum = int(input())
arr = list(map(int,input().split()))
if len(arr)<2:
    result = -1
else:
    arr.sort()
    if(arr[0]+arr[1]<=sum):
        result =arr[0]*arr[1]
    else:
        result = 0
print(result)