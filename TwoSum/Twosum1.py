'''Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
'''
Given a dictionary used to store the list's values and index
key is number, values is index. [13,12,11]-->{13:0,12:1,11:2}
for i , n in enumerate(nums):
    lookup the dictionary's value via list.get(target-n) # require no duplication and no none
    return the result once found
    
'''
#drawback: store the list into a dictionary, if a list have two or three same integer, it can just contain a latest value
#but it can work

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = dict([(number,index) for index, number in enumerate(nums)])
        for i, n in enumerate(nums):
            if list.get(target-n) !=i and list.get(target-n) != None:
                return [i+1,list.get(target-n)+1]