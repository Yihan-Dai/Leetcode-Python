'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
    
'''


'''
Note:
Nsum question can be handled using two pointer, O(N-1)
'''
#Here solution is using dictionary,*hash map
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = []
        if nums == list:
            return []
        dict = {}
        nums = sorted(nums)
        for index,value in enumerate(nums):
            dict[value] = index
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target = 0 - nums[i] - nums[j]
                if dict.get(target) >i and dict.get(target)!= None and dict.get(target) > j:
                    if [nums[i],nums[j],target] not in list:
                        list.append([nums[i],nums[j],target])
                
        
        return list