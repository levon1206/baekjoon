import sys
ssr = sys.stdin.readline
from collections import deque

N = int(ssr())
arr = [int(ssr()) for _ in range(N)]
arr = deque(arr)
stack = []
stack.append([arr.popleft(), 1])
ans = 0

while arr:
    t = arr.popleft()
    try:
        while stack[-1][0] < t: ans += stack.pop()[1]
        if stack[-1][0] > t:
            stack.append([t, 1])
            ans += 1
        else:
            if len(stack) > 1: ans += 1
            ans += stack[-1][1]
            stack[-1][1] += 1
    except: stack.append([t, 1])

print(ans)