#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz
#
# algorithms
# Easy (58.49%)
# Total Accepted:    88.4K
# Total Submissions: 151.1K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                results.append("FizzBuzz")
            elif num % 3 == 0:
                results.append("Fizz")
            elif num % 5 == 0:
                results.append("Buzz")
            else:
                results.append(str(num))
        
        return results
