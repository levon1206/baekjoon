n = int(input())
seq = list(map(int, input().split()))

index_stack = []
right_large_num = [-1 for _ in range(n)]

for i in range(n) :
    while True :
        if (not index_stack) or (seq[index_stack[-1]] >= seq[i]) :
            break
        right_large_num[index_stack.pop()] = seq[i]
    index_stack.append(i)

print(*right_large_num)