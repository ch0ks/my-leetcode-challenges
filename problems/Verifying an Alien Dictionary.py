#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 953. Verifying an Alien Dictionary
# Rank: Easy
# URL: https://leetcode.com/problems/verifying-an-alien-dictionary/
#
# In an alien language, surprisingly they also use english lowercase letters, but
# possibly in a different order. The order of the alphabet is some permutation of
# lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien
# language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
# Example 4:
#
# Input: words = ["kuvp","q"], order = "ngxlkthsjuoqcpavbfdermiywz"
# Output: true
# Explanation: Test case, no explanation
#
#
# Note:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
class Solution:
    def isAlienSorted(self, words, order):
        """
        Checks if the word input is an alien language.
        """
        for w_index in range(len(words) - 1):
            word_one = words[w_index]
            word_two = words[w_index + 1]

            for l_index in range(min(len(word_one), len(word_two))):
                # If they compare badly, it's not sorted.
                wo_letter = word_one[l_index]
                wt_letter = word_two[l_index]
                if wo_letter != wt_letter:
                    wo_letter_idx = order.index(wo_letter)
                    wt_letter_idx = order.index(wt_letter)
                    if wo_letter_idx > wt_letter_idx:
                        return False
                    break
            else:
                if len(word_one) > len(word_two):
                    return False

        return True


def main():
    the_solution = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(the_solution.isAlienSorted(words, order))

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(the_solution.isAlienSorted(words, order))

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    print(the_solution.isAlienSorted(words, order))

    words = ["kuvp", "q"]
    order = "ngxlkthsjuoqcpavbfdermiywz"
    print(the_solution.isAlienSorted(words, order))


if __name__ == "__main__":
    main()
