while True :
    first_num, second_num = map(int,input().split())
    if first_num == 0 and second_num == 0 :
        break

    if second_num % first_num == 0 :
        print("factor")
    elif first_num % second_num == 0 :
        print("multiple")
    else :
        print("neither")