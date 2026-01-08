from Solution import matrixSquare
from Solution import printMatrix

rowsNcolumns = int(input("Enter number of rows and columns: "))

symbol = input("Enter symbol to fill matrix: ")

matrix = matrixSquare(rowsNcolumns , symbol)


printMatrix(rowsNcolumns , matrix)



