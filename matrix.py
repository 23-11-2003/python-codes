"""n = int(input())
m = int(input())
i = 0
j = 0
a = []
for i in range(n):
    
    for j in range(m):
        max=a[i][j]>a[j][i]"""
    
n = int(input())
m = int(input())

# Initialize the matrix
a = []

# Input the matrix elements
for i in range(n):
    r = list(map(int, input().split()))  # Input each row
    a.append(row)

# Initialize the maximum value with the first element of the matrix
max = a[0][0]

# Loop through the matrix to find the maximum value
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            

# Output the maximum value
print(max)

