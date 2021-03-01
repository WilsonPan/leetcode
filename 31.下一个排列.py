#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
from typing import List, Literal


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums or len(nums) <= 1:
            return

        length = len(nums)

        if length == 2 or nums[length - 2] < nums[length - 1]:
            nums[length - 2], nums[length - 1] = nums[length - 1], nums[length - 2]
            return

        pointer = length - 3
        while pointer >= 0:
            if nums[pointer] < nums[pointer + 1]:
                break
            pointer = pointer - 1

        left = pointer + 1
        right = length - 1
        current_val = nums[pointer] if pointer >= 0 else 101
        is_swap = False

        while left <= right:

            if not is_swap and nums[right] > current_val:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                is_swap = True

            if not is_swap and nums[left] > current_val and nums[left + 1] <= current_val:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                is_swap = True

            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            pass


# @lc code=end

for i in range(4):
    for k in range(4):
        print(i)