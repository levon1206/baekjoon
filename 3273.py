n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

start, end = 0, n-1
cnt = 0

while start < end:
    summary = arr[start] + arr[end]
    if summary == x:
        cnt += 1
        start += 1
    elif summary > x:
        end -= 1
    elif summary < x:
        start += 1

print(cnt)