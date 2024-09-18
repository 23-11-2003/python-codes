
def OperationBinaryString(str):
    if str ==0:
        return -1
    ans=ord(str[0])-ord('0')
    for i in range(1,len(str),2):
        j = i+1;
        if(str[i]=='A'):
            ans = ans & (ord(str[i])-ord('0'))
        elif(str[i]=='B'):
            ans = ans | (ord(str[j])-ord('0'))
        elif(str[i]=='C'):
            ans = ans ^ (ord(str[j])-ord('0'))
    return ans 


str = input()
print(OperationBinaryString(str))

