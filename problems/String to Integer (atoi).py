#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 8. String to Integer (atoi)
# Rank: Medium
# URL: https://leetcode.com/problems/string-to-integer-atoi/
#
# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first
# non-whitespace character is found. Then, starting from this character, takes an optional
# initial plus or minus sign followed by as many numerical digits as possible, and
# interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace
# characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:
#
# Input: "42"
# Output: 42
# Example 2:
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−2^31) is returned.

import re


class Solution:
    def myAtoi(self, s):
        # First case: The string starts with a character. Not a sign nor a number
        if not re.search("^ *[0-9]+ *|^ *\+[0-9]+ *|^ *\-[0-9]+ *", s):
            return 0

        n_dict = []
        # I create my own dictionary
        for idx in range(0, 10, 1):
            n_dict.append(str(idx))

        is_neg = False
        n_found = False
        s_num = []
        for letter in s:
            # If this is true then is a number
            if letter == '-' and not n_found:
                is_neg = True
            elif letter == '+' and not n_found:
                is_neg = False
            elif letter in n_dict:
                s_num.append(n_dict.index(letter))
                n_found = True
            else:
                if n_found:
                    break

        n_final = 0
        n_ctr = 1
        # Now we convert the string into numbers:
        for number in reversed(s_num):
            n_final += (number * n_ctr)
            n_ctr *= 10

        # Case: There is a negative symbol. Then the number is negative
        if is_neg:
            n_final *= -1

        # Case: The number is within certain range
        bottom = (2 ** 31) * -1
        top = (2 ** 31) - 1
        if not (bottom <= n_final <= top):
            if n_final < 0:
                n_final = bottom
            else:
                n_final = top

        return n_final


def main():
    the_solution = Solution()
    s = "-13+8+7-345"  # Expected -1387345
    print(the_solution.myAtoi(s))
    s = "13+8-7"  # Expected -1387
    print(the_solution.myAtoi(s))
    s = "+13+8"  # Expected 138
    print(the_solution.myAtoi(s))
    s = "-13+8"  # Expected -138
    print(the_solution.myAtoi(s))
    s = "-   234"  # Expected 0
    print(the_solution.myAtoi(s))
    s = "32  aa +-2"  # Expected 21
    print(the_solution.myAtoi(s))
    s = "-45645 aa +-2"  # Expected -45645
    print(the_solution.myAtoi(s))
    s = "   +-2"  # Expected 0
    print(the_solution.myAtoi(s))
    s = "+-2"  # Expected 0
    print(the_solution.myAtoi(s))
    s = "    -42"
    print(the_solution.myAtoi(s))
    s = "42"
    print(the_solution.myAtoi(s))
    s = "4193 with words"
    print(the_solution.myAtoi(s))
    s = "words and 987"
    print(the_solution.myAtoi(s))
    s = "-91283472332"
    print(the_solution.myAtoi(s))
    s = "+9128347236732"
    print(the_solution.myAtoi(s))
    s = "+472332"
    print(the_solution.myAtoi(s))
    s = "12342 words words words 454545"
    print(the_solution.myAtoi(s))


if __name__ == "__main__":
    main()
