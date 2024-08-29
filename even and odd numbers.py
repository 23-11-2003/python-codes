list
list=[32,13,44,39,46,99,35,86]
even=[]
odd=[]
for i in list:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list:",even)
print("odd list:",odd)