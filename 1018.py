n, m = map(int, input().split())
w = [[0] * m for _ in range(n)]
b = [[0] * m for _ in range(n)]
arr = [list(input()) for _ in range(n)]
cnt = float('inf')

for i in range(n) :
    for j in range(m) :
        if not (i+j) % 2 :
            w[i][j] = 'W'
            b[i][j] = 'B'
        else :
            w[i][j] = 'B'
            b[i][j] = 'W'

for i in range(n - 7) :
    for j in range(m - 7) :
        tw, tb = 0, 0
        for x in range(8) :
            for y in range(8) :
                if arr[i + x][j + y] != w[i + x][j + y] :
                    tw += 1
                if arr[i + x][j + y] != b[i + x][j + y] :
                    tb += 1
        cnt = min(cnt, tw)
        cnt = min(cnt, tb)
print(cnt)