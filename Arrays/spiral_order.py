# rotating a matrix is equivalent to transposing a matrix (zip(*matrix))
# and inverting colums (to rotate right) or rows (to rotate left).

# separate top row
# rotate counter-clockwise
def spiral_right(matrix):
    if matrix:
        return list(matrix[0]) + spiral_right(list(zip(*matrix[1:]))[::-1]) 
    else:
        return []
        
# separate top row and invert it
# rotate clockwise
def spiral_left(matrix):
    if matrix:
        return list(matrix[0][::-1]) + spiral_left(list(zip(*matrix[1:][::-1]))) 
    else:
        return []

matrix = [[2,3,4,8],
        [5,7,9,12],
        [1,0,6,10]]

print("### ORIGINAL ###")
print(matrix)
print("### RIGHT ###")
print (spiral_right(matrix))
print("### LEFT ###")
print(spiral_left(matrix))
