'''Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.'''

'''Note: 
Roman numeric system
Roman numerals, as used today, are based on seven symbols:[1]

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1,000
Numbers are formed by combining symbols and adding the values, so II is two (two ones) and XIII is thirteen (a ten and three ones). There is no zero in this system and characters do not represent tens, hundreds and so on according to position as in 207 or 1066; those numbers are written as CCVII (two hundreds, a five and two ones) and MLXVI (a thousand, a fifty, a ten, a five and a one).

Symbols are placed from left to right in order of value, starting with the largest. However, in a few specific cases,[2] to avoid four characters being repeated in succession (such as IIII or XXXX), subtractive notation is often used as follows:[3][4]

I placed before V or X indicates one less, so four is IV (one less than five) and nine is IX (one less than ten)
X placed before L or C indicates ten less, so forty is XL (ten less than fifty) and ninety is XC (ten less than a hundred)
C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand)[5]
Combination	Value
IV	4
IX	9
XL	40
XC	90
CD	400
CM	900
For example, MCMIV is one thousand nine hundred and four, 1904 (M is a thousand, CM is nine hundred and IV is four).
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list = []
        list2 = [1000,500,100,50,10,5,1]
        str = ['M','D','C','L','X','V','I']
        str2 = ['M','D','C','L','X','V','I']
        newstr = ''
        for i in range(7):
            list.append(num/list2[i])
            num = num % list2[i]
        
        for i in range(7):
            if list[i] > 3 and list[i-1] ==1:
                list[i] = 1
                str[i-1] = str2[i]
                str[i] = str2[i-2]
            elif list[i] >3:
                list[i] = 1
                list[i-1] = 1
                str[i] = str2[i-1]
                str[i-1] = str2[i]
        for i in range(7):
            newstr = newstr+list[i]*str[i]
        return newstr