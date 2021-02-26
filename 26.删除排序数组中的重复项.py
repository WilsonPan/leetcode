#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        current, next = 0, 1

        while next < len(nums):
            if nums[current] != nums[next]:
                current = current + 1
                nums[current] = nums[next] if (next - current) > 0 else nums[current]
            next = next + 1
            pass

        return current + 1

        pass


# @lc code=end
