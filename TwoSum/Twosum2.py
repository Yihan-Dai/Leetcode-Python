'''Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
define list = {}
for n in range(len(nums)):
    if there's any target - nums[i] in list:
        return [list[target-num[i]]+1,i+1]
    else:
        store the right value(index i and num[i]) into list
        list[num[i]] = i
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target-nums[i]]+1, i +1]
            else:
                dict[nums[i]] = i