def fun(arr,len,num,diff):
    count = 0
    for i in range(len):
        if abs(num-arr[i])<=diff:
            count+=1
            return count
        else:
            return -1
        

len= int(input())
arr = list(map(int,input().split()))
num= int(input())
diff= int(input())
print(fun(arr,len,num,diff))