n =int(input())
sum = 0
for digit in str(n):
    sum +=int(digit)**len(str(n))
if sum == n:
    print("amstrong num")
else:
    print("not amstrong num")