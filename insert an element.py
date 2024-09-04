"""def add(n):
    print("10",n[2])
 
n = list(map(int,input().split()))
add(n)"""

"""ele={1,2,3,4,5}
new =4
pos =2 
temp = set()
i = 0
for elem in ele:
    if i == pos:
        temp.add(new)
    temp.add(elem)
    i +=1
print(temp)"""

a = list(map(int,input().split()))
b = 10
n = len(a)
result=[]

for i in range(n):
    if i == 2:
        result.append(b)
    if i < n:
        result.append(a[i])
print(" ".join(map(str,result)))
