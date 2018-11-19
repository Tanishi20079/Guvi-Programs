n=int(input())
s=list(map(int,input().split()))
if len(s) == n:
    print(max(s))
else:
    print("invalid")