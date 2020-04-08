# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    import math
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        totalArr = [head]
        current = head
        while current.next is not None:
            current = current.next
            totalArr.append(current)
        return totalArr[len(totalArr) / 2]
