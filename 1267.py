# Daily problem 23-01 https://leetcode.com/problems/count-servers-that-
# communicate/?envType=daily-question&envId=2025-01-23

from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def count_servers(grid: List[List[int]]) -> int:
        # list with the positions of the servers
        server_positions = []

        # column and row servers counter
        column_counter = defaultdict(int)
        row_counter = defaultdict(int)

        # iterate through the grid and save the servers positions, and
        # calculate the total amount of servers that are presents in each row
        # and column
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    server_positions.append((y, x))
                    row_counter[y] += 1
                    column_counter[x] += 1
        # get all the servers that its row or column has at least 2 servers
        return sum(
            1 for pos in server_positions
            if row_counter[pos[0]] >= 2 or column_counter[pos[1]] >= 2
        )
