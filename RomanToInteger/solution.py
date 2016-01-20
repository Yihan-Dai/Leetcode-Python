'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

'''
'''
Just remember there are three special cases:
1. IV,IX
2. CM,CD
3. XC,XL
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number,i = 0,0
        dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        while i < len(s):
            if i == len(s) -1:
                number += dict[s[i]]
                return number
            if dict[s[i]] ==100 and (dict[s[i+1]]==1000 or dict[s[i+1]]==500):
                number = number + dict[s[i+1]]-dict[s[i]]
                i += 2
            elif dict[s[i]] ==10 and (dict[s[i+1]]==100 or dict[s[i+1]]==50):
                number = number + dict[s[i+1]]-dict[s[i]]
                i += 2
            elif dict[s[i]] ==1 and (dict[s[i+1]]==10 or dict[s[i+1]]==5):
                number = number + dict[s[i+1]]-dict[s[i]]
                i += 2
            else:
                number += dict[s[i]]
                i +=1
        return number 