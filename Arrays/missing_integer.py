This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


def missing_integer(arr):
    arr.sort()
    idx = 0
    while idx < len(arr)-1:
        if arr[idx+1] >= 0 and arr[idx] >= 0 and arr[idx+1] - arr[idx] > 1:
            return arr[idx] + 1
        idx += 1
    return arr[idx] + 1

arr = [3, 4, -1, 1]
arr2 = [1, 2, 0]
print(missing_integer(arr))
print(missing_integer(arr2))
