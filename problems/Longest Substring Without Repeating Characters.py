#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 3. Longest Substring Without Repeating Characters
# Rank: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s):
        str_arr = []
        for i in s:
            if i not in str_arr:
                str_arr.append(i)
        if len(str_arr) == 1:
            return 1
        str_arr = []
        str_max_ctr = 0
        for i in s:
            if i not in str_arr:
                str_arr.append(i)
            else:
                char_index = str_arr.index(i)+1
                if len(str_arr) > str_max_ctr:
                    str_max_ctr = len(str_arr)
                if str_arr[len(str_arr) - 1] is i:
                    str_arr = [i]
                else:
                    for x in range(char_index):
                        str_arr.pop(0)
                    str_arr.append(i)
        if len(str_arr) > str_max_ctr:
            str_max_ctr = len(str_arr)
        return str_max_ctr


def main():
    the_solution = Solution()
    print(the_solution.lengthOfLongestSubstring("abcabcbb"))
    print(the_solution.lengthOfLongestSubstring("bbbbb"))
    print(the_solution.lengthOfLongestSubstring("pwwkew"))
    print(the_solution.lengthOfLongestSubstring("aab"))
    print(the_solution.lengthOfLongestSubstring("ckilbkd"))


if __name__ == "__main__":
    main()
