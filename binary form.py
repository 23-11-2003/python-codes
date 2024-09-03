n=int(input("enter a string:"))
while (n>0):
  i=n%10
  if (i==0 or i==1):
    print("binary")
    break
  else:
    print("not a binary number")
    break
