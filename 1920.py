n = int(input())
num_list = list(map(int,input().split()))
num_list.sort()
m = int(input())
test_num = list(map(int,input().split()))

for i in range(m) :
    search_num = test_num[i]
    start = 0
    end = n-1
    mid = (start+end)//2
    while start <= end :
        if search_num < num_list[mid] :
            end = mid - 1
            mid = (start+end)//2
        elif search_num > num_list[mid] :
            start = mid + 1
            mid = (start+end)//2
        elif  search_num == num_list[mid] :
            break
    if start <= end :
        print(1)
    else :
        print(0)