n=input()
s=''
for i in n:
    if i!=" ":
        s=i+s
    elif i==" ":
        print(s,end=" ")
        s=""
    else:
        continue
print(s)
