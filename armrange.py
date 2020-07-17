n1,n2=map(int,input().split())
for n in range(n1,n2):
    m=n
    s=0
    while n!=0:
        r=n%10
        s=s+r**3
        n=n//10
    if s==m:
          print(m)
  
