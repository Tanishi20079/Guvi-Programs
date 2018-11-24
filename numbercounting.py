n=int(input())
l=list(map(int,input().split()))
s=set(l)
a=[]
for i in s:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>1:
        a.append(i)
print(*sorted(a))
            
