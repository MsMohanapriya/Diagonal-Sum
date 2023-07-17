import numpy as np
def DiagonalSum(matrix):
    sum=0
    for i in range(row):
        sum+=matrix[i][i]
    print(sum)
    
    
array=list(map(int,input("enter matrix values: ").split()))
row=array[0]
column=array[1]
new_array=array[2:]
matrix=np.array(new_array).reshape(row,column)
print(DiagonalSum(matrix))
