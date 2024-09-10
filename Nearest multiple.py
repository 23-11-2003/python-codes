def RoundOff(n):
    remainder = n% 10
    if remainder <=4:
        return n - remainder
    else:
        return n +(10 - remainder)
    
n= int(input())
print(RoundOff(n))