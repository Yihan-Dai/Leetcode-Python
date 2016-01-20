'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

#recurrence accomplished using another function embedded in main function

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        list = [" ", "*", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        string = []
        result =[]
        if digits =="":
            return []
        def search(cur):
            if cur >= len(digits):
                result.append("".join(string))
            else:
                for i in list[int(digits[cur])]:
                    string.append(i)
                    search(cur+1)
                    string.pop()
        
        search(0)
        return result