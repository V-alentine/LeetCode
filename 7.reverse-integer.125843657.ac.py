#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer
#
# algorithms
# Easy (24.47%)
# Total Accepted:    310K
# Total Submissions: 1.3M
# Testcase Example:  '0'
#
# Reverse digits of an integer.
# 
# 
# Example1: x =  123, return  321
# Example2: x = -123, return -321
# 
# 
# click to show spoilers.
# 
# Have you thought about this?
# 
# Here are some good questions to ask before coding. Bonus points for you if
# you have already thought through this!
# 
# If the integer's last digit is 0, what should the output be? ie, cases such
# as 10, 100.
# 
# Did you notice that the reversed integer might overflow? Assume the input is
# a 32-bit integer, then the reverse of 1000000003 overflows. How should you
# handle such cases?
# 
# For the purpose of this problem, assume that your function returns 0 when the
# reversed integer overflows.
# 
# 
# 
# 
# 
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should
# return 0 when the reversed integer overflows.
# 
#
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer
#
# algorithms
# Easy (24.47%)
# Total Accepted:    310K
# Total Submissions: 1.3M
# Testcase Example:  '0'
#
# Reverse digits of an integer.
#
#
# Example1: x =  123, return  321
# Example2: x = -123, return -321
#
#
# click to show spoilers.
#
# Have you thought about this?
#
# Here are some good questions to ask before coding. Bonus points for you if
# you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such
# as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is
# a 32-bit integer, then the reverse of 1000000003 overflows. How should you
# handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the
# reversed integer overflows.
#
#
#
#
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should
# return 0 when the reversed integer overflows.
#
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        num = []

        if x < 0:
            sign = -1
        if x == 0:
            return 0
        x = abs(x)

        while x:
            num.append(x%10)
            x //= 10

        for i in num:
            res *= 10
            res += i

        if res > 0x7FffFFff:
            return 0
        else:
            return res * sign


