
"""n = list(map(int,input().strip().split()))
Max =0
for i in range(len(n)):
    if n[i] > Max :
        Max = n[i]
        index = i
print(Max)
print(index)"""


def findmax(arr):
    max_val = max(arr)
    max_ind = arr.index(max_val)
    print(max_val)
    print(max_ind)

arr = list(map(int,input().split()))
findmax(arr)