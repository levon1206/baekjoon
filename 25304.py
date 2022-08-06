R_price = int(input())
number = int(input())
N_price = 0

for _ in range(number) :
    price, nums = map(int, input().split())
    N_price += price * nums

if N_price == R_price :
    print("Yes")
else :
    print("No")