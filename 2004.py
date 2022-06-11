def count_2(num):
    cnt = 0
    while num != 0:
        num = num//2
        cnt += num
    return cnt

def count_5(num):
    cnt = 0
    while num != 0:
        num = num//5
        cnt += num
    return cnt

m, n = map(int, input().split())

print( min( count_2(m)-count_2(n)-count_2(m-n) , count_5(m)-count_5(n)-count_5(m-n)) )