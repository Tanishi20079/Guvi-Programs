t1,t2=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=0
for i in l2:
    if i in l1:
        c+=1
    else:
        c=0
        break
if c==0:
    print("NO")
else:
    print("YES")
    
