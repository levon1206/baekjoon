n = int(input())
nums = [int(input()) for i in range(n)]
nums.sort()

def gcd(x,y):
    if x%y == 0:
        return y
    return gcd(y,x % y)

a = []
for i in range(1,n):
    a.append(nums[i] - nums[i-1])
a.sort()

while(len(a)!=1):
    for i in range(1,len(a)):
        a[i-1] = gcd(a[i],a[i-1])
    a = a[:len(a)-1]
a = a[0]

result = [a]
for i in range(2,int(a**0.5)+1):
    if a%i == 0:
        result.append(i)
        result.append(a//i)
print(*sorted(list(set(result))))