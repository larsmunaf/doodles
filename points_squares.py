# count squares in a given matrix

def points_squares(matrix):
    size_x = len(matrix[0])
    size_y = len(matrix)
    count = 0

    for i in range(0, size_y):
        for j in range(0, size_x):
            offset = 1
            while offset < size_x - j and offset < size_y - i:
                if matrix[i+offset][j] == 1 and matrix[i][j+offset] == 1:
                    count += 1
                    offset += 1
                else:
                    break

    return count
        

def main():
    matrix1 = [[1,1,1], [1,1,1], [1,1,1]]
    print(points_squares(matrix1))

main()
