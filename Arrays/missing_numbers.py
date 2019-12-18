#this problem was asked by Two Sigma.

#You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. Find the missing 1000 numbers. What is the computational and space complexity of your solution?

def missingNumbers(arr):
    original = set(arr)
    res = []
    for i in range(min(arr), max(arr)):
        if i not in original:
            res.append(i)
    return res

arr = [x for x in range(1, 1000001) if x not in [45,12,78,55,105,768,514,225]]
print(missingNumbers(arr))
