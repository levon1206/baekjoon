n = int(input())
a = []
dp = [0 for _ in range(n)]
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort()
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1] and dp[i]< dp[j]:
            dp[i] = dp[j]
    dp[i] +=1

print(n-max(dp))