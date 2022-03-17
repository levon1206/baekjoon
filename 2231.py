n = int(input())

c = 0
start = max(n - 9 * len(str(n)), 0)
for i in range(start, n) :
    if n == sum(map(int, str(i))) + i :
        c = i
        break
print(c)