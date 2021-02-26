#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0

        current = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[current] = nums[i]
                current = current + 1
            pass
        return current
        pass
# @lc code=end

