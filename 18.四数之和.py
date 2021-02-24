#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if not nums or len(nums) < 4:
            return []

        nums.sort()
        res: List[List[int]] = []

        length = len(nums)
        print(length)
        for i in range(length - 3):
            print('i', i)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target):
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue

            for k in range(i + 1, length - 2):
                print('k', k)
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue

                if (nums[i] + nums[k] + nums[k + 1] + nums[k+2]) > target:
                    break
                if (nums[i] + nums[k] + nums[length - 1] + nums[length-2]) < target:
                    continue

                left, right = k + 1, length - 1

                while left < right:
                    total = nums[i] + nums[k] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[k], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right - 1]:
                            right = right - 1
                        left, right = left + 1, right - 1
                    elif total > target:
                        right = right - 1
                    else:
                        left = left + 1
                    pass
                pass

        return res

# @lc code=end


nums = [1, -2, -5, -4, -3, 3, 3, 5]

target = -11

print(Solution().fourSum(nums, target))
