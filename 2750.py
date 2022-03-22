N = int(input())

num = []

for i in range(N) :
    A = int(input())
    num.append(A)

num.sort()

for i in range(N):
    print(num[i])