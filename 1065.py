def is_han(number: int):
    number = str(number)
    if len(number) == 1 or len(number) == 2:
        return True
    else :
        lst = list()
        for i in number:
            lst.append(int(i))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            return True
        else :
            return False

num = int(input())
cnt = 0
for i in range(1,num+1):
    if is_han(i) == True:
        cnt = cnt + 1
print(cnt)