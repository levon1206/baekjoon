import sys 
n = int(input())
check_is = [0] * 10001

for _ in range(n) :
    num = int(sys.stdin.readline())
    check_is[num] = check_is[num] + 1

for i in range(10001) :
    if check_is[i] != 0 :
        for _ in range(check_is[i]) :
            print(i)