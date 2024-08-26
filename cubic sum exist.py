def isCubicSumExist(A, N):
    count = 0
    for z in A:
        for x in range(1, int(z**(1/3))+1):
            for y in range(x, int((z-x**3)**(1/3))+1):
                if x**3 + y**3 == z:
                    count += 1
                    break
            if count > 0:
                break
    return count

N = int(input())
A = list(map(int, input().split()))
print(isCubicSumExist(A, N))                           