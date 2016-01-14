'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = nums1+nums2
        new = sorted(array)
        if len(new)%2 == 0:
            index1 = len(new)/2 -1
            index2 = len(new)/2 
            return float(new[index1] + new[index2])/2
        else:
            index = (len(new)+1)/2 -1
            return float(new[index])