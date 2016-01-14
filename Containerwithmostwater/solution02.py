'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

'''

#two pointer O(n) and O(1)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        ls,rs = 0 , len(height) - 1
        while rs > ls:
            newarea = min(height[ls],height[rs]) * (rs - ls)
            maxarea = max(maxarea, newarea)
            if height[ls]>height[rs]:
                rs -= 1
            else:
                ls += 1
        return maxarea