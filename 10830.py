import sys
input = sys.stdin.readline

n, B = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

def dac(s,b):
    if b == 1:
        return s

    a = dac(s,b//2)
    cal = []
    for i in range(n):
        temp = []
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * a[k][j]
            temp.append(num%1000)
        cal.append(temp)
    result = []
    if b % 2:

        for i in range(n):
            temp = []
            for j in range(n):
                num = 0
                for k in range(n):
                    num += cal[i][k] * A[k][j]
                temp.append(num%1000)
            result.append(temp)
    else:
        result = cal

    return result
for i in dac(A,B):
    for j in i:
        print(j%1000, end =" ")
    print()