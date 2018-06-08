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

set = [3, 34, 4, 12, 5, 2]
sum = 9
subSetSum(set,sum)
