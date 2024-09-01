def ConvertToPalindrome(L):
    le = len(L)
    for i in range(le):
        if L[i] != L[le - i - 1]:
            L.insert(le - i, L[i])
        else:
            break

        s = "".join(L)
        if s == s[::-1]:
            return s

    return "".join(L)

s1 = input().strip()
L = list(s1)
print(ConvertToPalindrome(L))
