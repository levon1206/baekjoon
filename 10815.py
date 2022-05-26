N = int(input())
sanggeun_card = list(map(int,input().split()))
sanggeun_card.sort()

M = int(input())
compare_card = list(map(int,input().split()))

result = ""
for i in range(M) :
    start = 0
    mid = N // 2
    end = len(sanggeun_card) - 1
    while start <= end:
        if compare_card[i] == sanggeun_card[mid]:
            result += "1 "
            break
        elif compare_card[i] < sanggeun_card[mid] :
            end = mid - 1
            mid = (start + end) // 2
        else :
            start = mid + 1
            mid = (start + end) // 2
    if start > end :
        result += "0 "

print(result)