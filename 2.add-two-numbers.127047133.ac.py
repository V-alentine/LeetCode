#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# algorithms
# Medium (28.05%)
# Total Accepted:    378.4K
# Total Submissions: 1.3M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
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
        p, q = l1, l2
        carry = 0
        head = cur = ListNode(0)
        
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            
            val = x + y + carry
            carry = val / 10
            
            cur.next = ListNode(val % 10)
            cur = cur.next
            
            if p:   p = p.next 
            if q:   q = q.next
            
        if carry:
            cur.next = ListNode(carry)
            
        return head.next
