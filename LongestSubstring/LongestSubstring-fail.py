#Given a string, find the length of the longest substring without repeating characters. 
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
#which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        index = 0
        dict = {}
        Length = 0
        length = 0
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
                index += 1
                length = index
            else:
                length = index
                index = i - dict[s[i]]
                k = dict[s[i]]
                while k >=0:
                    if k in dict.values():
                        del dict[s[k]]
                    k -=1
                        
                dict[s[i]] = i
            if Length <= length:
                Length = length
        return Length