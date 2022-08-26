import heapq
import sys
input = sys.stdin.readline

n = int(input())

array = []
brray = []

for _ in range(n):
    a = int(input())

    if len(array) == len(brray):
        heapq.heappush(array,-a)
    else:
        heapq.heappush(brray,a)

    if len(array) > 0 and len(brray) > 0 and -array[0] > brray[0]:
        heapq.heappush(brray,-heapq.heappop(array))
        heapq.heappush(array,-heapq.heappop(brray))

    print(-array[0])