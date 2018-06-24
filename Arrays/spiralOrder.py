# separate top row
# Transpose and flip upside-down (rotate counter-clockwise)
def spiralOrder(matrix):
    if matrix:
        return list(matrix[0]) + spiralOrder(list(zip(*matrix[1:]))[::-1]) 
    else:
        return []

arr2 = [[2,3,4,8],
        [5,7,9,12],
        [1,0,6,10]]

print (spiralOrder(arr2))
