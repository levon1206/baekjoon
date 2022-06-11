test_case = int(input())
for _ in range(test_case) :
    num_cloth = int(input())
    clothes = {}
    all_set = 1
    for _ in range(num_cloth) :
        cloth = input().split()
        type_cloth = cloth[1]
        if type_cloth in clothes :
            clothes[type_cloth] =clothes[type_cloth] + 1
        else :
            clothes[type_cloth] = 2
    for i in clothes.values() :
        all_set *= i
    print(all_set - 1)
