#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 345. Reverse Vowels of a String
# Rank: Medium
# URL: https://leetcode.com/problems/reverse-vowels-of-a-string/
#
# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        This function will reverse any string.

        :param s: the string to reverse.
        :return: the reversed string.
        """

        s_vowels = []
        s_vowels_dict = "aeiouAEIOU"

        # First we extract the vowels from the original string and add them in order in a temporary list.
        for letter in s:
            if letter in s_vowels_dict:
                s_vowels.append(letter)

        # Now we walk through the original string again and if we find a vowel we extract the last one from the
        # temporary list and add it to the original string.
        s_final = ""
        for letter in s:
            if letter in s_vowels_dict:
                s_final += s_vowels.pop(-1)
            else:
                s_final += letter

        return s_final


def main():
    my_solution = Solution()
    s = "hello"
    print(my_solution.reverseVowels(s))
    s = "leetcode"
    print(my_solution.reverseVowels(s))
    s = "aA"
    print(my_solution.reverseVowels(s))


if __name__ == "__main__":
    main()
