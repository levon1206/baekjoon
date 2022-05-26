import sys

input = sys.stdin.readline
N, M = map(int,input().split())
compare_list = [input() for _ in range(N)]

test_list = [input() for _ in range(M)]

cnt = 0
for word in test_list:
    if word in compare_list :
        cnt += 1
print(cnt)