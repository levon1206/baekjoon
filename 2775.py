t = int(input())

for _ in range(t):
    a = int(input())
    b = int(input())
    num = [i for i in range(1 , b + 1)]
    for _ in range(a):
        for i in range(1 , b):
            num[i] += num[i - 1]
    print(num[-1])