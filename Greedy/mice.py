def mice(A, B):
    A.sort()
    B.sort()
    times = []
    for i in range(0,len(A)):
        times[i] = abs(A[i]-B[i])
    return max(times)

A = [4,-4,2]
B = [4,0,5]
print(mice(A,B))
    