n = int(input())
a = list(map(int, input().split()))
sum_num = [a[0]]

for i in range(len(a) - 1):
    sum_num.append(max(sum_num[i] + a[i + 1], a[i + 1]))

print(max(sum_num))