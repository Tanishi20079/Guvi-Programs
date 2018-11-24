n=int(input())
l=list(map(int,input().split()))
a=[]
c=0
for i in range(0,len(l)):
        if i==l[i]:
            a.append(i)
            c=+1
if c==0:
    print("-1")
else:
    print(*a)