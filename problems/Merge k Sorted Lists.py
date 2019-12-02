#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 23. Merge k Sorted Lists
# Rank: Hard
# URL: https://leetcode.com/problems/merge-k-sorted-lists/
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):

        list_tmp = []
        root_nodes = node_iterator = ListNode(0)
        for node in lists:
            while node:
                list_tmp.append(node.val)
                node = node.next

        list_tmp.sort()
        for value in list_tmp:
            node_iterator.next = ListNode(value)
            node_iterator = node_iterator.next

        return root_nodes.next


def prepareListNodes(lists):
    list_nodes = []
    for v_list in lists:
        root = n_iter = ListNode(0)
        for value in v_list:
            n_iter.next = ListNode(value)
            n_iter = n_iter.next
        list_nodes.append(root.next)
    return list_nodes


def main():
    """
    This is the main program
    :return:
    """
    the_solution = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    list_nodes = prepareListNodes(lists)
    print(the_solution.mergeKLists(list_nodes))


if __name__ == "__main__":
    main()
