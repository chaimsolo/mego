def gettingNumbers(matrix, num_of_matrix):
    for i in range(3):
        for j in range(3):
            matrix[i][j] = "-"
            num = float(input("enter the number for {} \n{}\n{}\n{}\n>>>".format(num_of_matrix, matrix[0], matrix[1], matrix[2])))
            matrix[i][j] = num
    print(f"{matrix[0]}\n{matrix[1]}\n{matrix[2]}")
    return matrix

def calculater(matrix_a, matrix_b):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            result[i][j] = matrix_a[i][0] * matrix_b[0][j] + matrix_a[i][1] * matrix_b[1][j] + matrix_a[i][2] * matrix_b[2][j]

    return result


mtrich_a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mtrich_b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

mtrich_a = gettingNumbers(mtrich_a, "matrix a")
mtrich_b = gettingNumbers(mtrich_b, "matrix b")
result = calculater(mtrich_a, mtrich_b)

print("The result is \n{}\n{}\n{}".format(result[0], result[1], result[2]))