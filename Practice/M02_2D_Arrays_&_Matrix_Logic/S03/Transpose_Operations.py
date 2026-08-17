#867 Transpose of a matrix
'''from typing import List
def transpose( matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        res=[[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                res[j][i]= matrix[i][j]
        return res
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))'''