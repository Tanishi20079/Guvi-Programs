n1,n2=map(int,input().split())
for i in range(n1,n2):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
    if c==0:
        print(i,end=" ")

