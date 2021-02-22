#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return None
        
        hashtable = dict()
        for i, num in enumerate(nums):
            
            if target - num in hashtable:
                return [hashtable[target - num], i]
            
            hashtable[num] = i
        
        return []

        
        
# @lc code=end

nums = [1, 3, 5, 7, 9]
for i, num in enumerate(nums):
    print(i, num)