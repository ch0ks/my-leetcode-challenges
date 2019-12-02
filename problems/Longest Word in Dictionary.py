#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 720. Longest Word in Dictionary
# Rank: Easy
# URL: https://leetcode.com/problems/longest-word-in-dictionary/
#
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one
# character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].


class Solution:
    def longestWord(self, words) -> str:
        wordset = set(words)
        words.sort(key=lambda c: (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word
        return ""

def main() -> object:
    """

    :return:
    """
    the_solution = Solution()
    words = ["w","wo","wor","worl", "world"]
    print(the_solution.longestWord(words))
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(the_solution.longestWord(words))

if __name__ == "__main__":
    main()
