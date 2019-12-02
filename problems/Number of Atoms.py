#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 726. Number of Atoms
# Rank: Hard
# URL: https://leetcode.com/problems/number-of-atoms/
# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
#
# 1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.
#
# Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.
#
# Example 1:
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
#
# Example 2:
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
#
# Example 3:
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# Note:
#
# All atom names consist of lowercase letters, except for the first character which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

import re
import collections

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Seaparate in 4 groups:
        # * Name of atom, can be N or Mg + multiplier. Multiplier = 1 is implicit
        # * Open parenthesis
        # * Closed parenthesis + multiplier. Multiplier = 1 is implicit
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]

        for name, m1, parenthesis_open, parenthesis_close, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            elif parenthesis_open:
                stack.append(collections.Counter())
            elif parenthesis_close:
                top = stack.pop()
                for x in top:
                    stack[-1][x] += top[x] * int(m2 or 1)

        simple_formula = ""
        sorted_names = sorted(stack[-1])
        for name in sorted_names:
            if stack[-1][name] > 1:
                simple_formula += name + str(stack[-1][name])
            else:
                simple_formula += name

        return simple_formula


def main():
    """

    :return:
    """
    the_solution = Solution()
    print(the_solution.countOfAtoms("H2O"))
    print(the_solution.countOfAtoms("Mg(OH)2"))
    print(the_solution.countOfAtoms("K4(ON(SO3)2)2"))


if __name__ == "__main__":
    main()
