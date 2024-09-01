def calculate(n):
    if n < 2:
        return "No"

    # Calculate the sum of the digits
    sum_of_digits = 0
    temp = n
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10

    # Check if the sum of digits is a prime number
    if sum_of_digits < 2:
        return "No"
    
    for i in range(2, int(sum_of_digits**0.5) + 1):
        if sum_of_digits % i == 0:
            return "No"
    
    return "Yes"

n = int(input("Enter a number: "))
print(calculate(n))
