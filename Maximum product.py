#l1,l2,r1,r2 = map(int,input().split()) in one line
l1 = int(input())
l2 = int(input())
r1 = int(input())
r2 = int(input())

for i in range(l1,r1+1):
    for j in range(l2,r2+1):
        a = l1*l2
        b = l1*r1
        c = r1*r2
        d = l2*r2
        e = l2*r1
        f = l1*r2
print(max(a,b,c,d,e,f))