"""def ispalindrome(s):
    return s==s[::-1]
s="karaka"
ans=ispalindrome(s)
if ans:
    print("yes")
else:
    print("no")"""
 
"""def is_palindrome(s): #without using slicing
    length = len(s)
    
    # Convert string to a list of characters
    s_list = list(s)
    
    for i in range(length // 2):
        if s_list[i] != s_list[length - 1 - i]:
            return False
    
    return True

s = "karaka"
if is_palindrome(s):
    print("yes")
else:
    print("no")"""
        
        
"""s = input()    #without using string ans slice
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        print("Not a palindrome")
        break
    i += 1
    j -= 1
else:
    print("Palindrome")"""
    
string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

   
