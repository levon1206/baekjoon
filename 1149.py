n = int(input())
space = []
for i in range(n):
    space.append(list(map(int, input().split())))
for i in range(1, len(space)):
    space[i][0] = min(space[i - 1][1], space[i - 1][2]) + space[i][0]
    space[i][1] = min(space[i - 1][0], space[i - 1][2]) + space[i][1]
    space[i][2] = min(space[i - 1][0], space[i - 1][1]) + space[i][2]
print(min(space[n - 1][0], space[n - 1][1], space[n - 1][2]))