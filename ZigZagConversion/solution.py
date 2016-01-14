'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s =="" or numRows ==1:
            return s
        add = 2*numRows - 2
        list = s[0::add]
        for i in range(1,numRows -1):
            for j in range(i, len(s),add):
                list += s[j]
                if j+add-i*2 < len(s):
                    list += s[j+add-i*2]
        list += s[numRows-1::add]
        return list