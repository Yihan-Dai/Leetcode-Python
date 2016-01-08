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
        dict = {}
        l = len(s)
        index = 0
        maxl = 0
        for i in range(l):
            j = 0
            k = 0
            while i-j >=0 and i+j < l:
                if s[i-j] != s[i+j]:
                    break
                index = j*2 + 1
                j +=1
           
            if index > maxl:
                maxl = index
                dict[maxl] = s[i-(maxl-1)/2:i+(maxl-1)/2+1]
           
            while i - k>=0 and i+k+1 <l:
                if s[i-k] != s[i+k+1]:
                    break
                index = k*2 +2
                k +=1
            
            if index > maxl:
                maxl = index
                dict[maxl] = s[i-(maxl/2-1):i+maxl/2+1]
        
        return dict[maxl]
            