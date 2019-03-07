n=int(input())
l=list(map(int,input().split()))
count=1
c=count
ar=[]
for i in range(len(l)):
    if l[i-1]<l[i]:
        c+=1
    if c!=1:
        ar.append(c)
    if l[i-1]>l[i]:
        c=1
print(max(ar))

