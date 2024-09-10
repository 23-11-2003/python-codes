def calculate(arr,m):
    arr.sort()
    j = m - 1
    
    for i in range(m // 2):
        print(arr[i],arr[j],end=" ")
        j-=1
    
    # Print the middle element if the length of the array is odd
    if m % 2 == 1:
        print(a[j])

m = int(input())
arr = list(map(int, input().strip().split()))
calculate(arr,m)
