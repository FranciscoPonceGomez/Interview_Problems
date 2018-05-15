import math

def squareRoot(n):
    if n < 2: return n
    low, high = 0, n
    while low <= high:
        mid = low + (high - low)/2
        if mid * mid > n:
            high = mid - 1
        elif mid * mid < n:
            low = low + 1
        else: return mid
    return math.ceil(mid)

number = 300
print(squareRoot(number))