#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs
#
# algorithms
# Easy (40.35%)
# Total Accepted:    203.9K
# Total Submissions: 505.3K
# Testcase Example:  '1'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
#
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #base cases
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        one_step_before = 2
        two_step_before = 1
        all_ways = 0
        
        for i in range(2, n):
            all_ways = one_step_before + two_step_before
            two_step_before = one_step_before
            one_step_before = all_ways
            
        return all_ways
