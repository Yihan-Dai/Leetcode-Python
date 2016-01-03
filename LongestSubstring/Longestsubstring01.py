#Given a string, find the length of the longest substring without repeating characters. 
#For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
#which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

'''
This solution using the comparison of two lengths. 
Firstly, if there's no repeating character in dictionary, increase the length.
When meeting the replication, compute the minimums value of two length.
{
In this case, it has two situations. and implementation is the fundamental.
1. index+1. in this length,which is the no repeating character length plus 1, it should be the repeating one.
   if the length of two same character is less than it, achieve the the length of two repeating character.
2. i - dict[s[i]]. the length of two repeating character. May be we can find this is longer than index +1,
    after the first or more repeating in this case the 1 in 'index+1' should be a unique character.
}
'''

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
            if s[i] not in dict:
                index +=1
            else:
                index = min(index+1,i-dict[s[i]])
            dict[s[i]] = i
            result = max(result,index)
                
        return result