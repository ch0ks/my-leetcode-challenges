#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 726. Number of Atoms
# Rank: Hard
# URL: https://leetcode.com/problems/number-of-atoms/
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?


class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums_tmp = []
        n_size = len(nums)
        n_half = int(len(nums)/2)
        for idx_a in reversed(range(n_size)):
            idx_b = idx_a - n_half
            nums_tmp.append(nums[idx_b])
            nums_tmp.append(nums[idx_a])
            if idx_b == 0:
                break

        for i in range(len(nums)):
            nums[i] = nums_tmp[i]

        return nums


def main():
    the_solution = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    print(the_solution.wiggleSort(nums))

    nums = [1, 3, 2, 2, 3, 1]
    print(the_solution.wiggleSort(nums))


if __name__ == "__main__":
    main()