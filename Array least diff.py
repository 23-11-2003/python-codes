def leastdifference(arr,length,n):
    minDiff = abs(arr[0] - n)
    minDiffElement = arr[0]
    
    for i in range(1,length):
        diff = abs(arr[i]-n)
        if diff < minDiff:
            minDiff = diff
            minDiffElement = arr[i]
    return minDiffElement

length = int(input())
arr = list(map(int,input().split()))
n = int(input())
print(leastdifference(arr,length,n))