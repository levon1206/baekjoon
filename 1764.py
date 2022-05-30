import sys
input = sys.stdin.readline

N, M = map(int,input().split())

none_hear = set()
for _ in range(N) :
    none_hear.add(input().strip())

none_see = set()
for _ in range(M) :
    none_see.add(input().strip())

none_see_hear = sorted(list(none_hear&none_see))

print(len(none_see_hear))
for name in none_see_hear :
    print(name)