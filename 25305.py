student_num, N = map(int, input().split())
score = list(map(int,input().split()))
score.sort(reverse=True)

print(score[N-1])