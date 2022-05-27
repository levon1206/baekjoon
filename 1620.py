import sys

input = sys.stdin.readline
N, M = map(int,input().split())

Pocket_collector_key_name = {}
Pocket_collector_key_number = {}
num = 1

for _ in range(N) :
    monster = input().strip()
    Pocket_collector_key_number[num] = monster
    Pocket_collector_key_name[monster] = num
    num += 1

for _ in range(M) :
    search = input().strip()
    try:
        print(Pocket_collector_key_number[int(search)])
    except :
        print(Pocket_collector_key_name[search])