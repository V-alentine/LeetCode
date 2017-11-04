#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# algorithms
# Easy (35.76%)
# Total Accepted:    670.4K
# Total Submissions: 1.9M
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for value_1 in range(0, len(nums)-1):
            for value_2 in range(value_1+1, len(nums)):
                if nums[value_1] + nums[value_2] == target:
                    return[value_1, value_2]
            
        
