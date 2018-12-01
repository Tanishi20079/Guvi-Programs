def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

n=input()
s=reverse(n)
if s==n:
    print("YES")
else:
    print("NO")