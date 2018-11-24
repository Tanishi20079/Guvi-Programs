n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
c=0
for i in l:
    if i==0:
        c+=1
if c==len(l):
    print("0")
else:
    for i in l:
        print(i,end='')