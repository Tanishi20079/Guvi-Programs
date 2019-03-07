n=int(input())
l=list(map(int,input().split()))
c=1
a=[]
for i in range(len(l)):
    if l[i-1]<l[i]:
        c+=1
    if c!=1:
        a.append(c)
    if l[i-1]>l[i]:
        c=1
print(max(a))

