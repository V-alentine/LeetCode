#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram
#
# algorithms
# Easy (46.80%)
# Total Accepted:    179.3K
# Total Submissions: 383.1K
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
