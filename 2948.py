# https://leetcode.com/problems/make-lexicographically-smallest-array-by-
# swapping-elements/description/

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        num_positions = [(num, index) for index, num in enumerate(nums)]
        num_positions.sort()
        groups = []
        new_group = [num_positions[0]]
        for prev, foll in zip(num_positions, num_positions[1:]):
            if foll[0] - prev[0] <= limit:
                new_group.append(foll)
            else:
                groups.append(new_group)
                new_group = [foll]
        if new_group:
            groups.append(new_group)
        returned_list = [0 for _ in range(len(nums))]
        for group in groups:
            positions = sorted(x[1] for x in group)
            numbers = [x[0] for x in group]
            for position, num in zip(positions, numbers):
                returned_list[position] = num
        return returned_list
