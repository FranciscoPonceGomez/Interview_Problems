def sameLevel(A):
    result = []
    stack = [A]
    while len(stack) > 0:
        result.append(stack.pop())
        if A.left:
            stack.append(A.left)
        if A.right:
            stack.append(A.right)

