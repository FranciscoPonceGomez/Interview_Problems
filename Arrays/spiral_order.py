# separate top row
# rotate counter-clockwise
def clockWise(matrix):
    if matrix:
        return list(matrix[0]) + clockWise(list(zip(*matrix[1:]))[::-1]) 
    else:
        return []

matrix = [[2,3,4,8],
        [5,7,9,12],
        [1,0,6,10]]

print (clockWise(matrix))
