import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n) :
    x = int(input())
    if x == 0 :
        if not heap :
             print(0)
        else :
            print(hq.heappop(heap))
    else :
        hq.heappush(heap, x)