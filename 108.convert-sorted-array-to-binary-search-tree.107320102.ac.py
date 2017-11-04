#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# algorithms
# Easy (42.61%)
# Total Accepted:    145.2K
# Total Submissions: 340.6K
# Testcase Example:  '[]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        left = 0
        right = len(nums)
        return self.array(nums, left, right)
        

    def array(self, nums, left, right):
        """
        :type nums: List[int]
        :type left: int
        :type right: int
        :rtype: TreeNode
        """
        if left == right:
            return None
            
        mid = left + (right - left)//2
        node = TreeNode(nums[mid])
        node.left = self.array(nums, left, mid)
        node.right = self.array(nums, mid+1, right)
        return node
