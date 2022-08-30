import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * n for i in range(n)]
s = list(map(int, input().split()))

for b in range(n):
    for start in range(n):
        end = start + b
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start + 1 == end:
            if s[start] == s[end]:
                dp[start][end] = 1
                continue
        if s[start] == s[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])