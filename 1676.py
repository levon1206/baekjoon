from math import factorial as fac
N = int(input())
Num = list(str(fac(N)))
Num.reverse()
cnt = 0
for _ in range(len(Num)) :
    if Num[0] == '0' :
        cnt += 1
        Num.remove(Num[0])
    else :
        break

print(cnt)