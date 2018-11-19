n=int(input())
s=list(map(int,input().split()))
if len(s) == n:
    print(*sorted(s))
else:
    print("invalid")