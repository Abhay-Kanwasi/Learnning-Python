# Add two matrices

matrix1 = [[1,2,3],
           [1,2,3],
           [1,2,3]]

matrix2 = [[1,2,4],
           [1,2,4],
           [2,3,4]]

sum = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        sum[i][j] = matrix1[i][j] + matrix2[i][j]
for num in sum:
    print(num)