class Solution: 
    def sumTwo(self, A, number):
        i = 0
        j = len(A)-1
        while i < j:
            if A[j] + A[i] == number:
                return [A[j],A[i]]
            elif A[j] + A[i] < number:
                i += 1
            else:
                j -= 1
        return [-1]
    
    def sumN(self, A, N, number):
        if(N > 2):
            for a in A:
                partial = self.sumN(A, N-1, number-a)
                if len(partial) == 1:
                    continue
                return [a, partial]
        else:
            return self.sumTwo(A, number)
        
test = Solution()
print(test.sumN([0,2,2,3,8], 4, 15))