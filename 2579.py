n = int(input())

s = [0 for i in range(301)]
score_sum = [0 for i in range(301)]

for i in range(n):
    s[i] = int(input())

score_sum[0] = s[0]
score_sum[1] = s[0] + s[1]
score_sum[2] = max(s[1] + s[2], s[0] + s[2])

for i in range(3, n):
    score_sum[i] = max(score_sum[i - 3] + s[i - 1] + s[i], score_sum[i - 2] + s[i])

print(score_sum[n - 1])