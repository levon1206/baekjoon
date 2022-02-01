N=int(input())
a=list(map(int, input().split()))

m=0
for i in range(N):
    if m<a[i]:
        m=a[i]

for i in range(N):
    a[i]=(a[i]/m)*100

s=0
for i in range(N):
    s+=a[i]

print(s/N)