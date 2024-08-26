def Average(s):
    n = len(s)
    sum = 0
    for i in s:
        sum = sum + ord(i)
    avg = sum/n   
    return avg   #otherwise we can directly write sum/len(str) without line 2 & 6

s = input()
temp = Average(s)
rounded_number = format(temp,".2f")
print(rounded_number)