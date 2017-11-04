#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate
#
# algorithms
# Easy (46.18%)
# Total Accepted:    180.5K
# Total Submissions: 390.8K
# Testcase Example:  '[]'
#
# 
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

