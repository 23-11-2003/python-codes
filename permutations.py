#using library
"""from itertools import permutations
s = input()
p = permutations(s)
for i in p:
    print(''.join(i))"""
    
def permute(s):
    if len(s) == 0:
        return [""]
    result = []
    for i in range(len(s)):
        for p in permute(s[:i] + s[i+1:]):
            result.append(s[i] + p)
    return result

s = input("Enter a string: ")
for permutation in permute(s):
    print(permutation)
