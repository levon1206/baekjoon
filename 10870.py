n = int(input())

A = [0,1]

for i in range(2,n+1):
    B = A[i-2] + A[i-1]
    A.append(B)

print(A[n])