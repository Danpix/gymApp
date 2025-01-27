import random
import pruebapy_utils as prueba

rows = int(input("Insert matrix row size: "))
columns = int(input("Insert matrix column size: "))

matrix = prueba.createRandomMatrix(rows, columns)

for result_row in matrix:
    print(result_row)