import sys
import heapq as hq
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        print(hq.heappop(heap)[1] if len(heap) else 0)
    else:
        hq.heappush(heap, (abs(x), x))