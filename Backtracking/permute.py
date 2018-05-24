def permute(A,index):
    if index == len(A):
        print(A)
    for j in range (index,len(A)):
        A[index],A[j] = A[j],A[index]
        permute(A,index+1)
        A[index],A[j] = A[j],A[index]

def permute2(str, prefix):
    if len(str) == 0:
        print(prefix)
    else:
        for i in range(0,len(str)):
            rem = str[0:i] + str[i+1:]
            # Add this line to create combinations too
            #print(prefix)
            permute2(rem, prefix + str[i])


A = ['A','B','C','D']
B = "ABCD"
permute(A,0)
permute2(B,"")
