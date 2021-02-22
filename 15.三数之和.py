#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. sort
        2. specially
        3. for + two points (left = i + 1 , right = len - 1)
            3.1 nums[i] > 0     : return , because
            3.2 i + left + right == 0   : add to res && skip same value
            3.3 i + left + right < 0    : left++
            3.4 i + left + right > 0    : right--
        """
        nums.sort()  # O(NlogN)

        n = len(nums)

        res: List[List[int]] = []

        for i in range(n):  # O(N)

            if nums[i] > 0:
                return res

            if(i > 0 and nums[i] == nums[i-1]):
                continue

            left = i + 1
            right = n - 1

            while (left < right):  # O(N)

                if (nums[i] + nums[left] + nums[right]) == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip same
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    # skip same
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif (nums[i] + nums[left] + nums[right]) < 0:
                    left = left + 1
                else:
                    right = right - 1
        return res
# @lc code=end
