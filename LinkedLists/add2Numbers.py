#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.toNum(l1)
        num2 = self.toNum(l2)
        return self.toLinkedList(num1+num2)
        
        
    def toNum(self, l):
        curr = l
        stack = []
        res = 0
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
        i = len(stack)-1
        while len(stack) > 0:
            res += pow(10,i)*stack.pop()
            i -= 1
        return res
    
    def toLinkedList(self, num):
        digits = [int(d) for d in str(num)]
        digits = digits[::-1]
        return digits
            