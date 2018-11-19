n=int(input())
s=list(map(int,input().split()))
if len(s) == n:
    print(min(s))
else:
    print("invalid")