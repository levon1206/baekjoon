N=int(input())

cnt=0

for i in range(N):
    A=input()
    E=0
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            NA=A[i+1:]
            if A[i] in NA:
                E += 1
    if E == 0:
        cnt += 1
print(cnt)