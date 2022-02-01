n=[]
for i in range(10):
    A=int(input())
    C=A%42
    n.append(C)
s=set(n)
print(len(s))