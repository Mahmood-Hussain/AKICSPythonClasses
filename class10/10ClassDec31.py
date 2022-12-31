def print_mat_elements(mat):
    rows = len(mat) 
    for i in range(0, rows):
        row = mat[i]
        columns = len(row)
        print(row)
        for j in range(0, columns):
            print(row[j], end=", ")


matrix1 = [[1, 4, 6], [8, 9, 0], [44, 2, 0]]
print_mat_elements(matrix1)