import sys
input = sys.stdin.readline

S = list(input().strip())
q = int(input())
result = ""

alpSum = []
alphabet = [0]*26

for val in S:
        alphabet[ord(val) - 97] += 1
        alpSum.append(alphabet[:])

for _ in range(q):
    a,l,r = input().split()
    l = int(l)
    r = int(r)
    tmp = 0

    tmp = alpSum[r][ord(a) - 97]
    if l != 0:
        tmp -= alpSum[l-1][ord(a) - 97]
    result += str(tmp) + "\n"

print(result)