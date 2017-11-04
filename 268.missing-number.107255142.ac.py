#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number
#
# algorithms
# Easy (44.31%)
# Total Accepted:    138.7K
# Total Submissions: 313K
# Testcase Example:  '[0]'
#
# 
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# 
# For example,
# Given nums = [0, 1, 3] return 2.
# 
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
# 
# 
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n*(n+1)/2 - sum(nums)
