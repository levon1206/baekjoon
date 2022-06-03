numbers = list(map(int,input().split()))
numbers.sort()

div_numbers = []
div_num = 2
least = 1

while div_num <= numbers[0] :
    if (numbers[0] % div_num == 0) and (numbers[1] % div_num == 0) :
        div_numbers.append(div_num)
        numbers[0] = numbers[0]/div_num
        numbers[1] = numbers[1]/div_num
        div_num = 2
    else :
        div_num += 1

for i in range(len(div_numbers)) :
    least *= div_numbers[i]
print(least)
print(int(least * numbers[0] * numbers[1]))