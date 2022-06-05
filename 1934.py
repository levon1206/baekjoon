N = int(input())

for _ in range(N) :
    numbers = list(map(int,input().split()))
    numbers.sort()

    dived_num = numbers[1]
    div_num = numbers[0]
    r = 1
    while r != 0 :
        r = dived_num % div_num
        dived_num, div_num = div_num, r

    print(int(numbers[1]*numbers[0]/dived_num))