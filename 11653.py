n = int(input())
a = 2
m = n
while True:
    if a > m:
        break
    if m % a == 0:
        print(a)
        m //= a
    else:
        a += 1
