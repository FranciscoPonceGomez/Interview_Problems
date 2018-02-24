
class Solution:
	def rotateMatrix(self, A):
		return zip(*A[::-1])

test = Solution()
A = [
    [3, 1],
    [4, 2]
]

print(test.rotateMatrix(A))
