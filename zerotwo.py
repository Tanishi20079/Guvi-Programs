t=int(input())
n=list(map(int,input().split()))
l=len(n)
for i in range(0,l-1):
    for j in range(i+1,l):
        if (n[i]+n[j])==0:
            print(n[i],"",n[j])
