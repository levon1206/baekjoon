A = int(input())
B = int(input())

S = []
for num in range(A,B+1):
    error = 0
    if num >1 :
        for i in range(2,num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            S.append(num)

if len(S) > 0:
    print(sum(S))
    print(min(S))
else:
    print(-1)