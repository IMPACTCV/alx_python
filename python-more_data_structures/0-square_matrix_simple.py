def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = [list(row) for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square of each integer in the input matrix
            new_matrix[i][j] = matrix[i][j] ** 2
    # Return the new matrix with squared values
    return new_matrix

print(square_matrix_simple( [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]))
