'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


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
        carry = 0
        result = None
        while l1 is not None or l2 is not None or carry ==1:
            value = 0
            if l1 is not None:
                value += l1.val
                l1 = l1.next
            if l2 is not None:
                value += l2.val
                l2 = l2.next
            value += carry
            digit = value % 10
            carry = value / 10
            if result is None:
                result = ListNode(digit)
                res = result
            else:
                res.next = ListNode(digit)
                res = res.next
        return result