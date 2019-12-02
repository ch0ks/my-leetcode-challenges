#!/user/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Name: 5255. Cells with Odd Values in a Matrix
# Rank: Easy
# URL: https://leetcode.com/contest/weekly-contest-162/problems/cells-with-odd-values-in-a-matrix/
#
#Given n and m which are the dimensions of a matrix initialized by zeros and given an
# array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to
# increment all cells in row ri and column ci by 1.
#
# Return the number of cells with odd values in the matrix after applying the increment
# to all indices.
#
#
#
# Example 1:
#
#
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# Example 2:
#
#
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
#
#
# Constraints:
#
# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m


class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        matrix = []
        for i in range(n):
            matrix.append([0] * m)

        for index in indices:
            for row in range(n):
                row_index = index[0]
                col_index = index[1]
                if row == row_index:
                    for i in range(m):
                        matrix[row][i] += 1
                matrix[row][col_index] += 1
        odd_ctr = 0
        for row_matrix in  matrix:
            for element in row_matrix:
                if (element % 2) != 0:
                    odd_ctr += 1

        return odd_ctr



def main():
    the_solution = Solution()
    n = 2
    m = 3
    indices = [[0, 1], [1, 1]]
    print(the_solution.oddCells(n, m, indices))

    n = 2
    m = 2
    indices = [[1, 1], [0, 0]]
    print(the_solution.oddCells(n, m, indices))

if __name__ == "__main__":
    main()

