n=int(input())
m=n
s=0
while n!=0:
    r=n%10
    s=s+r**3
    n=n//10
if s==m:
    print("yes")
else: 
    print("no")
