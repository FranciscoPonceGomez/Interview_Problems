def subSetSum(set,sum):
    def aux(set,n,sum):
        if sum == 0:
            return True
        if sum != 0 and n == 0:
            return False
        if set[n-1] > sum:
            return aux(set,n-1,sum)
        return aux(set,n-1,sum) or aux(set,n-1,sum-set[n-1])

    print(aux(set,len(set),sum))

def subSetSumIter(arr, target):
    sums = set([0])
    for value in arr:
        new_sums = set()
        for s in sums:
            if s + value == target: 
                return True
            if s + value < target: 
                new_sums.add(s+value)
        
        for s in new_sums:
            sums.add(s)
    return False

set = [3, 34, 4, 12, 5, 2]
sum = 9
subSetSum(set,sum)
