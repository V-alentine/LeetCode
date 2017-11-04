#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number
#
# algorithms
# Easy (40.98%)
# Total Accepted:    138.8K
# Total Submissions: 338.7K
# Testcase Example:  '1'
#
# Write an algorithm to determine if a number is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Example: 19 is a happy number
# 
# 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# 
# 
# Credits:Special thanks to @mithmatt and @ts for adding this problem and
# creating all test cases.
#
class Solution(object):
    def digitSquareSum(self, n):
        """
        "type n: int
        "rtype: int
        """
        ret = 0
        while n:
            digit = n % 10
            n = n / 10
            ret += digit ** 2
        return ret
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.digitSquareSum(n)
        fast = self.digitSquareSum(n)
        fast = self.digitSquareSum(fast)
        
        while slow != fast:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
        
        if slow == 1:
            return True
        else:
            return False
        
