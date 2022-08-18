import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for i in range(9)]

loc = [[i,j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def dfs(n):
    if n == len(loc):
        for i in sudoku:
            print(*i)
        sys.exit(0)
        return

    row,col = loc[n]
    nums = [i for i in range(1,10)]

    for i in sudoku[row]:
        if i in nums:
            nums.remove(i)

    for i in range(9):
        if sudoku[i][col] in nums:
            nums.remove(sudoku[i][col])

    a,b = row//3, col//3
    for i in range(a*3, (a+1)*3):
        for j in range(b*3, (b+1)*3):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])

    for i in nums:
        sudoku[row][col] = i
        dfs(n+1)
    sudoku[row][col] = 0

dfs(0)