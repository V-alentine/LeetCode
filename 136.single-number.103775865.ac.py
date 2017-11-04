#
# [136] Single Number
#
# https://leetcode.com/problems/single-number
#
# algorithms
# Easy (54.86%)
# Total Accepted:    248.2K
# Total Submissions: 452.4K
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
# 
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)

