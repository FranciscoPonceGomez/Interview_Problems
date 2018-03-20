import itertools
class Solution:
    def maxSubArray(self, A):
        min_sum = max_sum = 0
        for sum in itertools.accumulate(A):
            min_sum = min(min_sum, sum)
            max_sum = max(max_sum, sum - min_sum)
        return max_sum
    
    def max_subarray_Kadane(self, A):
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

test = Solution()
print(test.maxSubArray([1,-233,79,46,85,-112,200]))
print(test.max_subarray_Kadane([1,-233,79,46,85,-112,200]))