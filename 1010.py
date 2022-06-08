from math import factorial as fac
N = int(input())

for _ in range(N) :
    L, R = map(int,input().split())
    result = fac(R)/(fac(L)*fac(R-L))
    print(int(result))