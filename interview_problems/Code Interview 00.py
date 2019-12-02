#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: Facebook Portal Code Interview
# This is the test I was given by Jake Sherin


def isParenthesis(my_character):
    return (my_character == ")") or (my_character == "(")


def isValidString(my_string):
    ctr = 0
    for i in my_string:
        if i == "(":
            ctr += 1
        elif i == ")":
            ctr -= 1

    return cnt == 0


def balance(str):
    """
    Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing unbalanced parentheses. You cannot add anything to the string to balance it, and you cannot use recursion.

    Your solution must account for both open and closed parentheses on both sides as well.

    Examples:
        ")())(()()("       -> "()()()"
        ")))))()(((((("    -> "()"
        "a(b(c((()(d(e(f(" -> "abc()def"
        "()"               -> "()"
        "a(b)c)"           -> "a(b)c"
        ")("               -> ""
        "((((("            -> ""
        "(()()("           -> "()()"
        ")a(b(c)d)e("           -> "a(b(c)d)e"


    There can be multiple correct results per input, for example:
        balance("(())())") -> "(()())" or "(())()"
    As long as your solution keeps only the balanced parentheses then
    it doesn't matter which solution you produce.
    """


    # Write code here
    # ")())(()()("       -> "()()()"
    # ")))))()(((((("    -> "()"
    # "a(b(c((()(d(e(f(" -> "abc()def"
    # "()"               -> "()"
    # "a(b)c)"           -> "a(b)c"
    # ")("               -> ""
    # "((((("            -> ""
    # "(()()("           -> "()()"
    # ")a(b(c)d)e("           -> "a(b(c)d)e"
    # (a()(  -> "a()"
    # )a())  -> "a()"
    # (a))(  -> "(a)"

    #
    # right_par = False
    # left_par = False
    # str_arr = []
    # n = len(str)
    # ctr = 0
    #
    # # checking if there is an apha numeric
    # char_flag = False
    # for i in str:
    #     if i.isalpha():
    #         char_flag = True
    #         break
    #
    # # If the parenthesis is incomplete, return empty string.
    # if '(' not in str and not char_flag:
    #     return ""
    # if ')' not in str and not char_flag:
    #     return ""
    # while ctr < n:
    #
    #     if ctr == 0 and str[ctr] == '(' or isalpha(str[ctr]):
    #         str_arr.append(str[0])
    #     else:
    #         if strp[ctr] == '(' and (str[ctr - 1] == ')' or isalpha(str[ctr - 1])):
    #             str_arr.append(str[0])
    #
    #         if strp[ctr] == ')' and (str[ctr - 1] == '(' or isalpha(str[ctr - 1])):
    #             str_arr.append(str[0])
    #
    #         if isalpha(str[ctr]) and (strp[ctr - 1] == ')'):
    #             str_arr.pop(ctr - 1)
    #             str_arr.append(str[0])
    #
    #         if isalpha(str[ctr]) and isalpha(str[ctr - 1]):
    #             str_arr.append(str[0])
    #
    # ctr += 1
    # return str_arr


def main():
    print(balance(")())(()()("))


if __name__ == "__main__":
    main()
