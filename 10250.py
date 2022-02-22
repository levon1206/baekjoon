T = int(input())

for i in range(T):
    H, W ,N = map(int, input().split())
    F = 0
    ho = 0
    if N % H == 0:
        F = H * 100
        ho = N // H
    else:
        F = (N % H) * 100
        ho = 1 + N // H
    print(F + ho)