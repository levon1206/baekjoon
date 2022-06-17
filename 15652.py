N, M = list(map(int,input().split()))

numbers = []

def add_number(num):
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return

    for i in range(num, N+1):
        numbers.append(i)
        add_number(i)
        numbers.pop()

add_number(1)