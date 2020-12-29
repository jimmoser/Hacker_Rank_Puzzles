import numpy as np
n = int(input("How many rows/columns in your nxn matrix? "))
row_num = 1
matrix = []
while row_num <= n:
    row_vals = str(input("What are the values for the row? "))
    row_list = list(map(float, row_vals.split(" ")))
    matrix.append(row_list)
    row_num += 1
print(matrix)
print(round(np.linalg.det(matrix),2))