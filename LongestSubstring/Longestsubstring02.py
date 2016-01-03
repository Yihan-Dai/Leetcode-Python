#Given a string, find the length of the longest substring without repeating characters. 
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
#which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

'''
This solution uses the cursor.
Before the first repeating situation, firstly we can find the maximum length of no repeating character,
which is i - cursor(initiated to be 0) + 1.
Then, finding repeating, we should move the cursor to the right of the repeating character which is stored in
the dictionary, that is given by cursor = dict[s[i]]+1. Then we can compute the length of no repeating by
i - cursor +1.
Note that one more case should be considered that in the second repeating, may be we find dict[s[i]]
 is less than the cursor. In this case, we just should consider the repeating character in the right of the 
 cursor, so just ignore it.
'''
# using cursor is a much easier solution i think.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        result = 0
        dict = {}
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= index:
                index = dict[s[i]] +1
                
            dict[s[i]] = i
            result = max(i - index+1,result)
                
        return result