import sys
sys.setrecursionlimit(10**9)
def Fac(n) :
    if n == 0 :
        return 1
    else :
        return n*Fac(n-1)

N, K = map(int, input().split())
factorial = Fac(N) // ( Fac(K) * Fac(N-K) )
print( int(factorial % 10007) )