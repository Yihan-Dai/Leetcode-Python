 '''
 Given a string S, find the longest palindromic substring in S. 
 You may assume that the maximum length of S is 1000,
 and there exists one unique longest palindromic substring.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns = '$#'+'#'.join(s)+'#_' 
        p=[0]*4000
        mx = 0
        id = 0
        maxl = 0
        newid = 0
        for i in range(1,len(ns)-1):
            if mx>i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 1
            
            while ns[i-p[i]] == ns[i+p[i]]:
                p[i] +=1
            
            if i+p[i] >mx:
                mx = i+p[i]
                id = i
            if maxl < p[i]:
                newid = i
                maxl = p[i]
        return s[newid/2 - maxl/2:newid/2-maxl/2+maxl-1]