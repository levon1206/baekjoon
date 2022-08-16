def mul(a, b):
    tmp = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += a[i][k] * b[k][j]
            tmp[i][j] %= 1000000007

    return tmp

def power(b, m):
    if b == 1:
        return m
    else:
        tmp = power(b // 2, m)

        if b % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), m)

N = 2
P = int(input())
M = [[1, 1], [1, 0]]
print(power(P, M)[0][1])