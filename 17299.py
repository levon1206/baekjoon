import heapq
n = int(input())
s = list(map(int,input().split()))
re = [-1]*n
dic = {}

for i in s:
    try:
        dic[i]+=1
    except:
        dic[i]=1

h = []
for i in range(n-1,-1,-1):
    while h:
        if len(h)!=1 and h[0][0]==dic[s[i]]:
            a = heapq.heappop(h)
            re[i]=a[1]
        elif h[0][0]>dic[s[i]]:
            re[i] = h[0][1]
            break
        else:
            heapq.heappop(h)
    heapq.heappush(h,(dic[s[i]],s[i]))

print(*re)