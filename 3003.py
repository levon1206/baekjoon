origin = [1,1,2,2,2,8]
num = list(map(int,input().split()))
result = ""

for i in range(len(origin)) :
    result += str(origin[i]-num[i]) + " "

print(result)
