'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    
'''

#using two pointers

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list =[]
        if nums == list:
            return list
        nums = sorted(nums)
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                target1 = nums[i] + nums[k]
                target2 = target -target1
                m = k+1
                n = len(nums) -1
                while m < n: 
                    if nums[m] + nums[n] == target2:
                        if [nums[i],nums[k],nums[m],nums[n]] in list:
                            m +=1
                        else:    
                            list.append([nums[i],nums[k],nums[m],nums[n]])
                            m +=1
                    elif nums[m] + nums[n] >target2:
                        n -=1
                    else:
                        m +=1
                            
        return list