n =int(input())
A = map(int,input().split())
B = 0
for N in A:
    error = 0
    if N > 1:
        for i in range(2,N):
            if N % i == 0:
                error += 1
        if error == 0:
            B += 1
print(B)