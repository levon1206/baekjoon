l = [list(map(int, input().split())) for i in range(int(input()))]
rankl = [0]*len(l)

for i in range(len(l)) :
    rank = 1
    x, y = l[i]
    for j in l :
        if j[0] > x and j[1] > y :
            rank += 1

    rankl[i] = str(rank)
print(" ".join(rankl))