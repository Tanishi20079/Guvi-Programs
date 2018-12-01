t=int(input())
n=list(map(int,input().split()))
a=[]
for i in range(t):
    if n[i]%2==0 and i%2!=0:
        a.append(n[i])
    elif n[i]%2!=0 and i%2==0:
        a.append(n[i])
    else:
        continue
print(*a)   