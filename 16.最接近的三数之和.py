#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        length = len(nums)
        res: int = nums[0] + nums[1] + nums[2]
        for i in range(length-2):
            left = i + 1
            right = length - 1
            while left < right:
                total = (nums[i] + nums[left] + nums[right])
                if abs(target - total) < abs(target - res):
                    res = total

                if target == total:
                    return total
                elif total > target:
                    right = right - 1
                else:
                    left = left + 1

        return res


# @lc code=end
