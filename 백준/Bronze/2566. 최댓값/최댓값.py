A = []
max_val = 0
max_row= 0
max_col=0

for _ in range(9):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(9):
    for col in range(9):
        if A[row][col] >= max_val:
            max_val= A[row][col]
            max_row=row+1
            max_col=col+1

print(max_val)
print(max_row,max_col)
