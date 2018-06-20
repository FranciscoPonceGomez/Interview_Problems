#[0, -1, 3, 100, 70, 50]

#=> 70*50*100 = 350000
# @param A : list of integers
# @return an integer
def maxp3(A):
    A.sort()
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])
    
test = [0, -1, 3, 100, 70, 50]
print(maxp3(test))