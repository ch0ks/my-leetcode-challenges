#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 1249. Minimum Remove to Make Valid Parentheses
# This was the coding test I had with Facebook for the Portal team Nov 7, 2019
# URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """

        final_str = ""
        ignore = []
        for i in range(len(s)):
            ignore.append(False)

        left = 0
        for i in range(len(s)):
            character = s[i]
            if character == '(':
                left += 1
            elif character == ')':
                if left > 0:
                    left -= 1
                else:
                    ignore[i] = True

        right = 0
        for i in reversed(range(len(s))):
            character = s[i]
            if character == ')':
                right += 1
            elif character == '(':
                if right > 0:
                    right -= 1
                else:
                    ignore[i] = True

        for i in range(len(s)):
            if not ignore[i]:
                final_str += s[i]

        return final_str


"""
The main program.
:return:
"""

solution = Solution()
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
print(solution.minRemoveToMakeValid("a)b(c)d"))
print(solution.minRemoveToMakeValid("))(("))
print(solution.minRemoveToMakeValid("(a(b(c)d)"))
print(solution.minRemoveToMakeValid(")())(()()("))
print(solution.minRemoveToMakeValid(")))))()((((((" ))
print(solution.minRemoveToMakeValid("a(b(c((()(d(e(f("))
print(solution.minRemoveToMakeValid("()"))
print(solution.minRemoveToMakeValid("a(b)c)"))
print(solution.minRemoveToMakeValid("(a()("))
print(solution.minRemoveToMakeValid(")a())"))
