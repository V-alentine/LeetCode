#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string
#
# algorithms
# Easy (59.48%)
# Total Accepted:    190K
# Total Submissions: 319.5K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
# 
# 
# Example:
# Given s = "hello", return "olleh".
# 
#
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
