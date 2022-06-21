melone = int(input())
field = []
for _ in range(6) :
    field.append(list(map(int,input().split())))

longest_w = 0
longest_h = 0
longest_w_location = 0
longest_h_location = 0

for i in range(len(field)) :
    if field[i][0] == 1 or field[i][0] == 2 :
        if longest_w < field[i][1] :
            longest_w = field[i][1]
            longest_w_location = i
    if field[i][0] == 3 or field[i][0] == 4 :
        if longest_h < field[i][1] :
            longest_h = field[i][1]
            longest_h_location = i

small_w = field[(longest_w_location - 1) % 6][1] - field[(longest_w_location + 1) % 6][1]
small_h = field[(longest_h_location - 1) % 6][1] - field[(longest_h_location + 1) % 6][1]
if small_w < 0 :
    small_w *= -1
if small_h < 0 :
    small_h *= -1
num_of_melones = ( (longest_w * longest_h) - (small_h * small_w) ) * melone
print(num_of_melones)