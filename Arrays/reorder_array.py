#This problem was asked by Google.
#Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.
#Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
#For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
#Hint: Try working backwards from the end state.

def push(array, el):
    array.insert(0, el)

def pop(array):
    if len(array) > 0:
        return array.pop()

def enqueue(array, el):
    array.append(el)

def dequeue(array):
    if len(array) > 0:
        el = array[0]
        array.remove(array[0])
        return el

def reorder_list(array):
    new_array = []
    while len(array) > 0:
        enqueue(new_array, dequeue(array))
        enqueue(new_array, pop(array)) if len(array) > 0 else None
    return new_array


print("[1, 2, 3, 4, 5, 6] => " + str(reorder_list([1,2,3,4,5,6])))
assert(reorder_list([1,2,3,4,5]) == [1,5,2,4,3])
