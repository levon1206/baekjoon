n, m = map(int, input().split())
num = list(map(int, input().split()))

start = 0
end = 0
answer = num[0]
cnt = 1
minimum = 1e+5+1

while start < n:
    if answer >= m:
        minimum = min(minimum, cnt)

    if answer >= m or end == n-1:
        answer -= num[start]
        start += 1
        cnt -= 1

    else:
        end += 1
        answer += num[end]
        cnt += 1
print(0 if minimum == 1e+5+1 else minimum)