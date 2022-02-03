from cgi import print_environ


c=int(input())
avg=[]

for i in range(c):
    n = list(map(int, input().split()))

    sum = 0
    for i in range(n[0]):
        sum += n[i + 1]

    cnt = 0
    for i in range(n[0]):
        if n[i + 1]>(sum/n[0]):
            cnt +=1

        avg.append((cnt / n[0]) * 100)
        n.clear()

for i in range(c):
    print("%.3f" %avg[i] + "%")