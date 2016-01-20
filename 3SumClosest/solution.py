'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
'''

#Using two pointers

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <=2:
            return []
        nums = sorted(nums)
        value = abs(target -nums[0] - nums[1] - nums[len(nums)-1])
        actual = nums[0] + nums[1] + nums[len(nums)-1]
        for i in range(len(nums)):
            lp = i+1
            rp = len(nums) -1

            while rp > lp:
                if nums[i] + nums[lp] + nums[rp] == target:
                    return target
                if nums[i] + nums[lp] + nums[rp] > target:
                    if abs(target -nums[i] - nums[lp] - nums[rp]) <= value:
                        value = abs(target -nums[i] - nums[lp] - nums[rp])
                        actual = nums[i] + nums[lp] + nums[rp]
                    rp -=1
                if nums[i] + nums[lp] + nums[rp] < target:
                    if abs(target -nums[i] - nums[lp] - nums[rp]) <= value:
                        value = abs(target -nums[i] - nums[lp] - nums[rp])
                        actual = nums[i] + nums[lp] + nums[rp]
                    lp +=1
            
        return actual