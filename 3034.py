N, W, H = map(int, input().split())
maxlength = W**2 + H**2
for _ in range(N) :
    length = int(input())
    if length**2 <= maxlength :
        print("DA")
    else :
        print("NE")
