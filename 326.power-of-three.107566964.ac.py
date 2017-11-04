#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three
#
# algorithms
# Easy (40.41%)
# Total Accepted:    106.6K
# Total Submissions: 263.8K
# Testcase Example:  '27'
#
# 
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
# 
# 
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0 and 3486784401 % n == 0:
            return True
        else:
            return False

