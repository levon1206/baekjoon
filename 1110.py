from ast import Num


N=int(input())
num=N
cnt=0
while 1:
    a=num//10
    b=num%10
    c=(a+b)%10
    num=(b*10)+c
    cnt=cnt+1
    if num==N:
        break
print(cnt)