def Ptriangle(A):
	for i in range (1,len(A)):
		for j in range(1,len(A[i])-1):
			A[i][j] = A[i-1][j] + A[i-1][j-1]
depth = 10
A = [[1]*(i+1) for i in range(10)]
Ptriangle(A)
print(A)
