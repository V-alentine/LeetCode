#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# algorithms
# Easy (39.84%)
# Total Accepted:    243.5K
# Total Submissions: 611.2K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# 
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_here = max_so_far = nums[0]
        
        for x in nums[1:]:
            max_here = max(x, max_here + x)
            max_so_far = max(max_here, max_so_far)
            
        return max_so_far
