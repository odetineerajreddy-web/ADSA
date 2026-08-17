'''#1351 count Negative Numbers in a Sorted Matrix 
from typing import List
def countNegatives_brute( grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            for ele in row:
                if ele < 0:
                    count+=1
        return count
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_brute(grid1))
'''
'''#Optimal solution
from typing import List
def countNegatives_optimal( grid: List[List[int]]) -> int:
    row,cols= len(grid) ,len(grid[0])
    count=0
    for r in range(row):
        for c in range(cols):
            if grid[r][c]<0:
                count+=(cols - c)
                break
    return count
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives_optimal(grid1))
    '''

    



            