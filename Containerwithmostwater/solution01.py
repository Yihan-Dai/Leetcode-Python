'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

'''
#O(n^2) time limit exceed

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                h = min(height[i],height[j])
                length = j - i 
                maxarea = max(maxarea,h*length)
                
        return maxarea