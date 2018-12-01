t=int(input())
n=list(map(int,input().split()))
a=[]
c=0
for i in n:
    if i in a:
        c=1
        break
    else:
        a.append(i)
if c==0:
    print("unique")
else:
    print(i)