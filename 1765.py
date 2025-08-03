# https://leetcode.com/problems/map-of-highest-peak/
# ?envType=daily-question&envId=2025-01-22

from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        lower_heights = set()
        current_max_height = 0
        current_heights = [[None for _ in isWater[0]] for _ in isWater]
        for y in range(len(isWater)):
            for x in range(len(isWater[0])):
                if isWater[y][x]:
                    lower_heights.add((y, x))
                    current_heights[y][x] = 0
        while lower_heights:
            current_max_height += 1
            new_lower_heights = set()
            for y, x in lower_heights:

                neighs = self.get_neigh(
                    current_heights, y, x
                )
                for y_, x_ in neighs:
                    current_heights[y_][x_] = current_max_height
                new_lower_heights.update(neighs)
            lower_heights = new_lower_heights
        return current_heights

    @staticmethod
    def is_valid_neigh(current_heights, y, x):
        if y < 0 or x < 0:
            return False
        try:
            return current_heights[y][x] is None
        except IndexError:
            return False

    def get_neigh(self, current_heights, y, x):
        neighs = []
        if self.is_valid_neigh(current_heights, y + 1, x):
            neighs.append((y + 1, x))
        if self.is_valid_neigh(current_heights, y - 1, x):
            neighs.append((y - 1, x))
        if self.is_valid_neigh(current_heights, y, x + 1):
            neighs.append((y, x + 1))
        if self.is_valid_neigh(current_heights, y, x - 1):
            neighs.append((y, x - 1))
        return neighs

