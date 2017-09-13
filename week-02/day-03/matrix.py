    # ['1', 'x'], 
    # ['2', 'x'], 
    # ['3', 'x']
    # ]
def creat_matrix():
    matrix  = []
    size = 4

    for i in range(size):
        row = []
        for j in range(size):
            row.append("0")
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    
    for matrix_row in range(len(matrix)):
        print(matrix[matrix_row])

finished = creat_matrix()
print_matrix(finished)



# print(matrix)
