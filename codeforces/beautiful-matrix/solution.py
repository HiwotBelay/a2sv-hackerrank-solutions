# Read the 5x5 matrix
matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1' in the matrix
# Matrix is 1-indexed in problem, but we use 0-indexed in code
one_row = 0
one_col = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            one_row = i
            one_col = j
            break

# The center is at position (2, 2) in 0-indexed (which is (3, 3) in 1-indexed)
# Minimum moves = Manhattan distance from current position to center
center_row = 2
center_col = 2

moves = abs(one_row - center_row) + abs(one_col - center_col)

print(moves)
