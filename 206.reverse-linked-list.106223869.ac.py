#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list
#
# algorithms
# Easy (46.01%)
# Total Accepted:    275.8K
# Total Submissions: 599.4K
# Testcase Example:  '[]'
#
# Reverse a singly linked list.
# 
# click to show more hints.
# 
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        former = None
        
        while head:
            latter = head.next
            head.next = former
            former = head
            head = latter
            
        return former
