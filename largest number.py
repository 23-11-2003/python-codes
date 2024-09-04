"""num1 = 10
num2 = 14
num3 = 12
if(num1>=num2) and (num1>=num3):
    print("largest is:",num1)
elif(num2>=num1) and (num2>=num3):
    print("largest is:",num2)
else:
    print("largest is:",num3)"""
    
"""n = int(input())
n1 = int(input())
n2 = int(input())
if (n > n1) and (n>n2):
    print("n is  greater")
elif (n1>n) and (n1>n2):
    print("n1 is greater")
else:
    print("n2 is greater")"""
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a, b, c)
print(f"The largest number is {largest}")
