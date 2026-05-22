# Matrix Operations

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Transpose
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("\nTranspose:")
for row in transpose:
    print(row)

# Sum of diagonal
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
print("\nDiagonal Sum:", diagonal_sum)
