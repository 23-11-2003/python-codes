"""def odd_digit_count(n):
    count = 0
    for i in range(1, n+1):
        digit_count = 0
        num = i
        while num > 0:
            digit_count += 1
            num = num // 10
        
        if digit_count % 2 != 0:
            count += 1
    
    return count  

n = int(input())
print(odd_digit_count(n))"""


def odd_digit_count(n):
    count = 0
    for i in range(1, n + 1):
        digit_count = len(str(i))
        if digit_count % 2 != 0:
            count += 1
    
    return count

n = int(input())
print(odd_digit_count(n))

