#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 159. Longest Substring with At Most Two Distinct Characters
# URL: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
#
# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = {}

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len


def main():
    the_solution = Solution()
    print(the_solution.lengthOfLongestSubstringTwoDistinct("leeeeeeeetcoooooooode"))  # Expected: 9
    print(the_solution.lengthOfLongestSubstringTwoDistinct("eceba"))  # Expected: 3
    print(the_solution.lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # Expected: 5
    print(the_solution.lengthOfLongestSubstringTwoDistinct("abababaabbcdcdcdcaaaab"))  # Expected: 10
    print(the_solution.lengthOfLongestSubstringTwoDistinct("ababacccccc"))  # Expected: 7


if __name__ == "__main__":
    main()

string




