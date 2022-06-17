N, M = list(map(int,input().split()))

numbers = []

def add_number():
    if len(numbers) == M:
        print(' '.join(map(str, numbers)))
        return

    for i in range(1, N+1):
        numbers.append(i)
        add_number()
        numbers.pop()

add_number()