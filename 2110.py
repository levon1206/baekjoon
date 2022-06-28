import sys
n,c = map(int,sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(n)]

house.sort()
start = 1
end = house[-1] - house[0]
result = 0

while start <= end:
    mid = (start+end)//2
    now = house[0]
    count = 1
    tmp = end
    for i in range(1, n):
        if now + mid <= house[i]:
            tmp = min(tmp, house[i]-now)
            count += 1
            now = house[i]

    if count < c:
        end = mid-1
    if count >= c:
        start = mid + 1
        result = max(result, tmp)

print(result)