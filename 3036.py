def gcd(a,b):
    while b != 0 :
        c = a%b
        a = b
        b = c
    return a

n = int(input())
num = list(map(int,input().split()))
first = num[0]
num.remove(first)

for i in range(len(num)) :
    gc = gcd(first,num[i])
    print(str(first//gc) + "/" + str(num[i]//gc))
