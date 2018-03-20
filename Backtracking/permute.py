def permute(A,index):
	if index == len(A)
	for j in range (index,len(A)):
		A[index],A[j] = A[j],A[index]
		permute(A,index+1)
		A[index],A[j] = A[j],A[index]

A = ['A','B','C','D']
permute(A,0)
