def Fac(n) :
    if n == 0 :
        return 1
    else :
        return n*Fac(n-1)

N, K = map(int, input().split())

print( int( Fac(N)/(Fac(K)*Fac(N-K)) ) )